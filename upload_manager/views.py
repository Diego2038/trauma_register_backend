from datetime import datetime, date, time
import time as count_time
import tempfile
import traceback
import os
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from .helpers.gestor_excel_file_data import GestorExcelFileData, GestorExcelSheetData
from .helpers.columns_configuration import columns_ubication, column_name_type_to_model, DataTypeCell, PatientData
from django.db.models import Model
from django.db.utils import DataError
from django.core.exceptions import ValidationError
from django.db import transaction

class UploadView(APIView):
  
  def post(self, request):
    init_time_endpoint = count_time.time() #? Calculate time
    serializer = UploadSerializer(data=request.data)
    file = request.data["file"]
    user_name: str = request.data["user"]
    update_data: bool = str(request.data["update_data"]).lower() == "true"
    print(f'LOG: Is it allowed to update data in the database?: {update_data}') 
    print(f'LOG: Execution time (Building Excel file)...') #? Calculate time 
    init_time = count_time.time() #? Calculate time
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_file:
      for chunk in file.chunks():
        temp_file.write(chunk)
      temp_file.flush()
    finish_time = count_time.time() #? Calculate time
    elapsed_time = finish_time - init_time  #? Calculate time
    print(f'LOG: Execution time (Excel file was built): {elapsed_time:.4f} seconds') #? Calculate time 
    
    gestor_excel_file_data = GestorExcelFileData(
      sheets_columns_configuration=columns_ubication,
      gestor_sheet=GestorExcelSheetData(),
      file_xls=temp_file.name,
    )
    
    try:
      result = gestor_excel_file_data.get_data_from_file()
      patients_key = 'Trauma Register:1'
      patients_data: list[dict[str,str]] = result.pop(patients_key)
      patients_to_be_updated: list[str] = []
      if update_data:
        patients_to_be_updated = self.delete_existing_data(patient_data=patients_data)
      patients_result: dict[str, list[dict[str, str]]]  = {patients_key: patients_data}
      self.save_elements_by_model(data_file=patients_result, column_name_type_to_model=column_name_type_to_model)
      users_not_found: list[str] = self.save_elements_by_model(data_file=result, column_name_type_to_model=column_name_type_to_model, existing_patients=patients_to_be_updated)
        
      if serializer.is_valid():
        return Response({
          "user": user_name,
          "allow_update_data": update_data,
          "updated_patients": patients_to_be_updated,
          # "result": {**result},
          "problems": users_not_found if len(users_not_found) else None,
        }, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as ve:
      return Response({
          "error": "The file has data that already exists in the database, please change the parameter \"allow_update_data\" with true or delete any data related to the patient ID",
          "allow_update_data": update_data,
          "specific_error": ve,
        }, status=status.HTTP_409_CONFLICT)
    except Exception as e:
      print(F"ERROR: {type(e)} - {e}")
      traceback.print_exc()
    
    finally:
      os.remove(temp_file.name)
      finish_time_endpoint = count_time.time() #? Calculate time
      elapsed_time = finish_time_endpoint - init_time_endpoint  #? Calculate time
      print(f'LOG: Time elapsed from "upload_manager/upload/" endpoint: {elapsed_time:.4f} seconds') #? Calculate time 
  
  def delete_existing_data(self, patient_data: list[dict[str,str]]) -> list[str]:
    repeteated_users: str = []
    for data in patient_data:
      try:
        id_patient = data["trauma_register_record_id"]
        patient = PatientData.objects.get(trauma_register_record_id=int(id_patient))
        repeteated_users.append(id_patient)
        patient.delete()
      except PatientData.DoesNotExist:
        continue
    print(f"LOG: Users to be updated: {len(repeteated_users)}")
    return repeteated_users
  
  
  def save_elements_by_model(self, data_file: dict[str, list[dict[str,str]]], column_name_type_to_model: dict[str,dict[str,Model|dict[str,DataTypeCell]]], existing_patients: list[str] = []) -> list[str]:
    error_key: str = None
    error_table: str = None
    error_id: str = None
    users_not_found_information: list[str] = []
    init_time = count_time.time() #? Calculate time
    try:
      for key_file in data_file:
        start_time = count_time.time() #? Calculate time
        error_table = key_file
        data_sheet = data_file[key_file]
        model = column_name_type_to_model[key_file]["model"]
        for data_row in data_sheet:
          if data_row["trauma_register_record_id"] in existing_patients: continue
          updated_data: dict[str,str|int|float|bool|datetime|date|time|PatientData|None] = {}
          for key_cell in data_row:
            error_key = key_cell 
            #! Here the data is converted according with their type
            data_type_cell: DataTypeCell = column_name_type_to_model[key_file]["type"][key_cell]
            data_cell: str = data_row[key_cell].strip()
            if data_cell == "None" or len(data_cell) == 0: continue
            if data_type_cell == DataTypeCell.STRING or data_type_cell == DataTypeCell.TEXT:
              updated_data[key_cell] = data_cell
            elif data_type_cell == DataTypeCell.INT:
              updated_data[key_cell] = int(data_cell)
            elif data_type_cell == DataTypeCell.DECIMAL:
              updated_data[key_cell] = float(data_cell)
            elif data_type_cell == DataTypeCell.BOOLEAN:
              boolean_result: bool | None
              if (data_cell.lower() == "si" or data_cell.lower() == "sí"):
                boolean_result = True
              elif (data_cell.lower() == "no"):
                boolean_result = False
              else:
                boolean_result = None
              updated_data[key_cell] = boolean_result
            elif data_type_cell == DataTypeCell.TIMESTAMP: #! It assumed that the format in excel file is saved as "DD/MM/YYYY hh:mm:ss" 
              obtained_data = data_cell.split(" ")
              obtained_date: list[str]
              if "/" in obtained_data[0]:
                obtained_date = obtained_data[0].split("/")
              elif "-" in obtained_data[0]:
                obtained_date = obtained_data[0].split("-")
              else:
                the_error = f"Date format is wrong, because this is the result: {obtained_data}"
                raise Exception(the_error)
              obtained_time = obtained_data[1].split(":")  
              obtained_date_time = datetime(
                year=int(obtained_date[2] if len(obtained_date[2]) == 4 else obtained_date[0]), #! change later, because it occurs only if the cell isn't general type
                month=int(obtained_date[1]), 
                day=int(obtained_date[0] if len(obtained_date[0]) == 2 else obtained_date[2]), #! change later, because it occurs only if the cell isn't general type
                hour=int(obtained_time[0]), 
                minute=int(obtained_time[1]), 
                second=int(obtained_time[2]),
                tzinfo=pytz.timezone(zone="America/Bogota")
              )
              updated_data[key_cell] = obtained_date_time
            elif data_type_cell == DataTypeCell.TIME: #! It assumed that the format in excel file is saved as "hh:mm:ss"
              obtained_data = data_cell.split(":")
              obtained_time = time(
                hour=int(obtained_data[0]), 
                minute=int(obtained_data[1]), 
                second=int(obtained_data[2]),
                tzinfo=pytz.timezone(zone="America/Bogota"),
              )
              updated_data[key_cell] = obtained_time
            elif data_type_cell == DataTypeCell.DATE: #! It assumed that the format in excel file is saved as "DD/MM/YYYY"
              
              obtained_data: list[str]
              if "/" in data_cell:
                obtained_data = data_cell.split("/")
              elif "-" in data_cell:
                obtained_data = data_cell.split("-")
              else:
                error = f"Date format is wrong"
                raise Exception(error)
              obtained_date = date(
                year=int(obtained_data[2]), 
                month=int(obtained_data[1]), 
                day=int(obtained_data[0]),
              )
              updated_data[key_cell] = obtained_date
            elif data_type_cell == DataTypeCell.FK:
              error_id = data_cell
              try:
                patient_data = PatientData.objects.get(trauma_register_record_id=int(data_cell))
                updated_data[key_cell] = patient_data
              except PatientData.DoesNotExist as e:
                error = f"PatienData in table <{error_table}> with key <{data_cell}> doesn't exist"
                users_not_found_information.append(error)
                updated_data[key_cell] = None
                break
          if updated_data["trauma_register_record_id"]: 
            try:
              model(**updated_data).save()
            except DataError as e:
              users_not_found_information.append(f"ERROR CREATION: In table: <{error_table}> with trauma_register_id: <{error_id}>): {e}")
        end_time = count_time.time() #? Calculate time
        elapsed_time = end_time - start_time  #? Calculate time
        print(f'LOG: Execution time (elements created from sheet called "{error_table}"): {elapsed_time:.4f} seconds') #? Calculate time 
          
    except KeyError as e:
      print(f"ERROR(save_element_by_model.py in table: <{error_table}> and attribute: <{error_key}>): DataTypeCell value doesn't exist, please establish the attribute {error_key} from the table{error_table} in columns_configuration.py with DataTypeCell enum")
      raise e
    except Exception as e:
      print(f"ERROR(save_element_by_model.py in table: <{error_table}> and attribute: <{error_key}> with trauma_register_id: <{error_id}>): {type(e)} - {e}")
      raise e
    finally:
      finish_time = count_time.time() #? Calculate time
      elapsed_time = finish_time - init_time  #? Calculate time
      print(f'LOG: Execution time (all elements created): {elapsed_time:.4f} seconds') #? Calculate time 
    return users_not_found_information