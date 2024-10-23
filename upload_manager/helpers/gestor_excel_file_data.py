import time
import traceback
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from .gestor_excel_sheet_data import GestorExcelSheetData

class GestorExcelFileData():
  
  def __init__(
    self, 
    sheets_columns_configuration: dict[str,dict[str,str]], 
    gestor_sheet: GestorExcelSheetData, 
    file_xls: str
    ):
    self.sheets_columns_configuration = sheets_columns_configuration
    self.gestor_sheet = gestor_sheet
    self.file_xls = file_xls
  
  def get_data_from_file(self) -> dict[str,list[dict[str,str]]]:
    """
    Extracts data from an Excel file based on the provided sheet and column configurations.

    This method iterates over each sheet defined in the `sheets_columns_configuration` dictionary.
    For each sheet, it calls the `get_data_from_sheet` method of the `gestor_sheet` object to
    extract the data based on the specified column mappings.

    Returns:
        dict[str,list[dict[str,str]]]: A dictionary where the keys are sheet names and the values
        are lists of dictionaries. Each inner dictionary represents a row of data, with keys
        corresponding to the name object and values being the cell values.

    Raises:
        Exception: If an error occurs during the data extraction process.
    """
    try:
      start_time = time.time() #? Calculate time
      workbook = openpyxl.load_workbook(self.file_xls)
      result_data_file : dict[str,list[dict[str,str]]] = {}
      for _, (key, value) in enumerate(self.sheets_columns_configuration.items()):
        updated_key = key.split(":")[0]
        sheet: Worksheet = workbook[updated_key]
        result_data_sheet : list[dict[str,str]] = self.gestor_sheet.get_data_from_sheet(
          column_ubication=value, 
          sheet=sheet,
        )
        result_data_file[key] = result_data_sheet
      end_time = time.time() #? Calculate time
      elapsed_time = end_time - start_time  #? Calculate time
      print(f"LOG: Execution time (all file's sheets): {elapsed_time:.4f} seconds") #? Calculate time 
      return result_data_file
      
      
    except Exception as e:
      print(f"ERROR: {str(e)} - {e}")
      traceback.print_exc()

    finally:
      workbook.close

### Use example

""" from columns_configuration import columns_ubication
try:
  file_xls = "./base_mini.xlsx"
  gestor_excel_file_data = GestorExcelFileData(
    sheets_columns_configuration=columns_ubication,
    gestor_sheet=GestorExcelSheetData(),
    file_xls=file_xls,
  )
  result = gestor_excel_file_data.get_data_from_file()
  # print(result)
  print()
  for key_sheet in result:
    for row_data in result[key_sheet]:
      patient = {**row_data}
      # last_key = next(reversed(row_data.keys()))
      print(f"{key_sheet} - {patient["trauma_register_record_id"]}")
    print("\n-----------------------\n")
    
except Exception as e:
  print(f"ERROR: Hubo un error: {e}")  """

  