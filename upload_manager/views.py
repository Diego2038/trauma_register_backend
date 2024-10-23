from django.shortcuts import render
import tempfile
import traceback
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from .helpers.gestor_excel_file_data import GestorExcelFileData, GestorExcelSheetData
from .helpers.columns_configuration import columns_ubication

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
      response_answer: dict[str,list[dict]] = {}
      for key_sheet in result:
        response_answer[key_sheet] = []
        for row_data in result[key_sheet]:
          patient = {**row_data}
          response_answer[key_sheet].append(patient['trauma_register_record_id'])
          # response_answer[key_sheet].append(patient)
          # last_key = next(reversed(row_data.keys()))
          
          print(f"{key_sheet} {patient['trauma_register_record_id']}")
        print("\n-----------------------\n")
      
      if serializer.is_valid():
        return Response({
          "user_name": user_name,
          "result": {**response_answer}
        }, status=status.HTTP_202_ACCEPTED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      print(F"ERROR: {type(e)} - {e}")
      traceback.print_exc()
    
    finally:
      os.remove(temp_file.name)