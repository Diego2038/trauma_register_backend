from openpyxl import cell
from openpyxl.worksheet.worksheet import Worksheet
import time #! delete later

class GestorExcelSheetData():
  
  def cell_get_value_with_str(self, cell_name: str, sheet: Worksheet, convert_str_answer=True ) -> str | None:
    """
    Retrieves the value of a specified cell in an Excel worksheet.

    Args:
      cell_name (str): The name of the cell (e.g., "A1").
      sheet (Worksheet): The Excel worksheet containing the cell.
      convert_str_answer (bool): If True, converts the cell value to a string.

    Returns:
      str|None: The cell's value as a string if converted, otherwise the original value, or None if empty.
    """
    cell_selected: cell = sheet[cell_name]
    return str(cell_selected.value) if convert_str_answer else cell_selected.value

  def get_row_elements(self, column_ubication: dict[str, str], sheet: Worksheet, row_number: int) -> dict:
    """
    Function to get all elements from a row in a sheet from an excel file
    Args:
      column_ubication (dict[str, str]): A dictionary mapping column names to their corresponding letter designations in the Excel sheet.
      sheet (Worksheet): The Excel worksheet you want to extract data from.
      row_number (int): The row number within the sheet from which you want to retrieve the elements.

    Returns:
      dict[str,str]: A dictionary containing the extracted elements, with column names as keys and their corresponding values as values.
    """
    result: dict[str,str] = {}
    for key in column_ubication:
      result[key] = self.cell_get_value_with_str(
        cell_name=f"{column_ubication[key]}{row_number}", 
        sheet=sheet,
      )
    return result

  def define_limit_row(self, sheet: Worksheet, selected_test_column: str = "A") -> int:
    """
      Determines the first empty row in a specified Excel worksheet.

      Args:
        sheet (Worksheet): The Excel worksheet to search.

      Returns:
        int: The index of the first empty row according with .
    """
    is_found_empty_space = False
    row = 2
    result = ""
    while not is_found_empty_space:
      result : str | None = self.cell_get_value_with_str(
        cell_name=f"{selected_test_column}{row}",
        sheet=sheet, 
        convert_str_answer=False,
      )
      if result != None:
        row += 1
        continue
      is_found_empty_space = True
    return row

  def get_data_from_sheet(self, column_ubication: dict[str,str], sheet: Worksheet, selected_test_column:str = "A") -> list[dict[str,str]]:
    """
    Extracts data from an Excel worksheet based on specified column mappings.

    Args:
      column_ubication (dict[str, str]): A dictionary mapping column headers to their corresponding cell names.
      sheet (Worksheet): The Excel worksheet from which to retrieve data.

    Returns:
      list[dict[str,str]]: A list of dictionaries, each representing a row of data with column headers as keys.
    """
    start_time = time.time() #? Calculate time
    max_row: int = self.define_limit_row(
      sheet=sheet,
      selected_test_column=selected_test_column,
    )
    result: list[dict[str,str]] = []
    for i in range(2, max_row):
      result.append(self.get_row_elements(
        column_ubication=column_ubication, 
        sheet=sheet, 
        row_number=i,
      ))
    end_time = time.time() #? Calculate time
    elapsed_time = end_time - start_time  #? Calculate time
    print(f"LOG: Execution time (sheet called \"{sheet.title}\"): {elapsed_time:.4f} seconds") #? Calculate time
    return result

### Use example
""" 
column_ubication : dict[str,str] = {
  "trauma_register_record_id": "A", 
  "direccion_linea_1": "G", 
  "direccion_linea_2": "H", 
  "ciudad": "I", 
  "canton_municipio": "J", 
  "provincia_estado": "K", 
  "codigo_postal": "L", 
  "pais": "M", 
  "edad": "N", 
  "unidad_de_edad": "O", 
  "genero": "P", 
  "fecha_de_nacimiento": "Q", 
  "ocupacion": "R", 
  "estado_civil": "S", 
  "nacionalidad": "T", 
  "grupo_etnico": "Y", 
  "otro_grupo_etnico": "Z", 
  "num_doc_de_identificacion": "AC", 
}

try:
  import openpyxl
  file_xls = "./base_mini.xlsx"
  workbook = openpyxl.load_workbook(file_xls)
  sheet: Worksheet = workbook["Trauma Register"]
  data = GestorExcelSheetData().get_data_from_sheet(column_ubication=column_ubication, sheet=sheet)
  for row_data in data:
    patient = {**row_data}
    print(f"Patient - {patient["trauma_register_record_id"]}, edad: {patient["edad"]}")
  
  
except Exception as e:
  print(f"Error de lectura: {str(e)} - {e}")

finally:
  workbook.close
  """