from datetime import datetime, date, time
import tempfile
import traceback
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from .helpers.gestor_excel_file_data import GestorExcelFileData, GestorExcelSheetData
from .helpers.columns_configuration import columns_ubication, column_name_type_to_model, DataTypeCell
from django.db.models import Model

class UploadView(APIView):
  
  def post(self, request):
    serializer = UploadSerializer(data=request.data)
    file = request.data["file"]
    user_name = request.data["user"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_file:
      for chunk in file.chunks():
        temp_file.write(chunk)
      temp_file.flush()
    
    gestor_excel_file_data = GestorExcelFileData(
      sheets_columns_configuration=columns_ubication,
      gestor_sheet=GestorExcelSheetData(),
      file_xls=temp_file.name,
    )
    
    try:
      result = gestor_excel_file_data.get_data_from_file()
      patients_key = 'Trauma Register:1'
      patients_data: list[dict[str,str]] = result.pop(patients_key)
      patients_result: dict[str, list[dict[str, str]]]  = {patients_key: patients_data}
      self.save_elements_by_model(data_file=patients_result, column_name_type_to_model=column_name_type_to_model) 
        
      if serializer.is_valid():
        return Response({
          "user_name": user_name,
          # "result": {**result},
          "result": {**patients_result}
        }, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print(F"ERROR: {type(e)} - {e}")
      traceback.print_exc()
    
    finally:
      os.remove(temp_file.name)
  
  def save_elements_by_model(self, data_file: dict[str, list[dict[str,str]]], column_name_type_to_model: dict[str,dict[str,Model|dict[str,DataTypeCell]]]):
    try:
      for key_file in data_file:
        data_sheet = data_file[key_file]
        model = column_name_type_to_model[key_file]["model"]
        for data_row in data_sheet:
          updated_data: dict[str,str|int|float|bool|datetime|date|time|None] = {}
          for key_cell in data_row:
            #! Here the data is converted according with their type
            data_type_cell: DataTypeCell = column_name_type_to_model[key_file]["type"][key_cell]
            data_cell: str | int | bool = data_row[key_cell].strip()
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
              date_and_time = data_cell.split(" ")
              obtained_date = date_and_time[0].split("/")
              obtained_time = date_and_time[1].split(":")
              obtained_date_time = datetime(
                year=int(data[2]), 
                month=int(data[1]), 
                day=int(data[0]), 
                hour=int(obtained_time[0]), 
                minute=int(obtained_time[1]), 
                second=int(obtained_time[2]),
              )
              updated_data[key_cell] = obtained_date_time
            elif data_type_cell == DataTypeCell.TIME: #! It assumed that the format in excel file is saved as "hh:mm:ss"
              obtained_time = data_cell.split(":")
              obtained_date_time = time(
                hour=int(obtained_time[0]), 
                minute=int(obtained_time[1]), 
                second=int(obtained_time[2]),
              )
              updated_data[key_cell] = obtained_date_time
            elif data_type_cell == DataTypeCell.DATE: #! It assumed that the format in excel file is saved as "DD/MM/YYYY"
              data = data_cell.split("/") 
              if len(data) < 3: continue
              obtained_date = date(
                year=int(data[2]), 
                month=int(data[1]), 
                day=int(data[0]),
              )
              updated_data[key_cell] = obtained_date
            else:
              raise f"ERROR: DataTypeCell value doesn't exist, please establish the attribute {key_cell} in columns_configuration.py with DataTypeCell enum"
          model(**updated_data).save()
    except Exception as e:
      print(F"ERROR(save_element_by_model): {type(e)} - {e}")
      raise e