import os
import tempfile
from django.test import TestCase
from unittest.mock import MagicMock, patch
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from rest_framework.exceptions import ParseError
from unittest.mock import MagicMock
from .helpers.gestor_excel_sheet_data import GestorExcelSheetData
from .helpers.gestor_excel_file_data import GestorExcelFileData


class GestorExcelSheetDataTest(TestCase):
  """
  Clase de pruebas unitarias para GestorExcelSheetData.
  """

  def setUp(self):
    """
    Configura el entorno de prueba. Se ejecuta antes de cada método de prueba.
    """
    self.gestor = GestorExcelSheetData()
    self.workbook = Workbook()
    self.sheet: Worksheet = self.workbook.active
    self.sheet.title = "Trauma Register"
    
    # Llenamos la hoja de cálculo con datos de prueba
    self.sheet['A1'] = 'Header1'
    self.sheet['B1'] = 'Header2'
    self.sheet['A2'] = 'Patient1'
    self.sheet['B2'] = 100
    self.sheet['A3'] = 'Patient2'
    self.sheet['B3'] = 200
    self.sheet['A4'] = None # Celda vacía para prueba de define_limit_row

  def test_cell_get_value_with_str_converts_to_string(self):
    """
    Prueba que el método convierte el valor de una celda a string correctamente.
    """
    # Prueba con un valor numérico
    result = self.gestor.cell_get_value_with_str(cell_name="B2", sheet=self.sheet)
    self.assertEqual(result, "100")
    
    # Prueba con un valor de texto
    result_str = self.gestor.cell_get_value_with_str(cell_name="A2", sheet=self.sheet)
    self.assertEqual(result_str, "Patient1")
      
  def test_cell_get_value_with_str_returns_original_value(self):
    """
    Prueba que el método retorna el valor original sin convertir si 'convert_str_answer' es False.
    """
    result = self.gestor.cell_get_value_with_str(cell_name="B2", sheet=self.sheet, convert_str_answer=False)
    self.assertEqual(result, 100)
      
  def test_get_row_elements(self):
    """
    Prueba que el método get_row_elements extrae los datos de una fila correctamente.
    """
    column_ubication = {"patient_id": "A", "age": "B"}
    row_number = 2
    
    expected_result = {"patient_id": "Patient1", "age": "100"}
    result = self.gestor.get_row_elements(
      column_ubication=column_ubication, 
      sheet=self.sheet, 
      row_number=row_number
    )
    self.assertEqual(result, expected_result)
      
  def test_define_limit_row(self):
    """
    Prueba que el método define_limit_row encuentra la primera fila vacía.
    """
    # La celda A4 está vacía en nuestro setUp
    expected_limit_row = 4 
    result = self.gestor.define_limit_row(sheet=self.sheet, selected_test_column="A")
    self.assertEqual(result, expected_limit_row)

  def test_get_data_from_sheet(self):
    """
    Prueba la función principal get_data_from_sheet.
    """
    # Mockeamos `define_limit_row` para evitar la lógica interna en esta prueba
    # Así probamos que `get_data_from_sheet` usa el valor del límite correctamente.
    self.gestor.define_limit_row = MagicMock(return_value=4)
    
    column_ubication = {"patient_id": "A", "age": "B"}
    
    expected_result = [
      {"patient_id": "Patient1", "age": "100"},
      {"patient_id": "Patient2", "age": "200"},
    ]
    
    result = self.gestor.get_data_from_sheet(
      column_ubication=column_ubication, 
      sheet=self.sheet
    )
    self.assertEqual(result, expected_result)

  def tearDown(self):
    """
    Limpia los recursos después de cada prueba.
    """
    self.workbook.close()

class GestorExcelFileDataTest(TestCase):
  """
  Clase de pruebas unitarias para GestorExcelFileData.
  """

  def setUp(self):
    """
    Configura el entorno de prueba.
    Crea un archivo de Excel temporal para simular la lectura.
    """
    # Configuramos los datos de prueba
    self.sheets_config = {
      "Hoja1:Datos": {"col1": "A", "col2": "B"},
      "Hoja2:Info": {"col3": "C", "col4": "D"},
    }

    # Creamos un archivo de Excel temporal para simular la lectura
    self.temp_dir = tempfile.mkdtemp()
    self.file_path = os.path.join(self.temp_dir, "test_file.xlsx")

    # Creamos el archivo de Excel con los nombres de hoja esperados
    workbook = Workbook()
    workbook.create_sheet("Hoja1")
    workbook.create_sheet("Hoja2")
    workbook.save(self.file_path)
    workbook.close()

  def tearDown(self):
    """
    Limpia los recursos temporales creados.
    """
    os.remove(self.file_path)
    os.rmdir(self.temp_dir)

  # --- Pruebas para el método inform_bad_format ---
  
  @patch('openpyxl.load_workbook')
  def test_inform_bad_format_raises_error_for_missing_sheet(self, mock_load_workbook):
    """
    Prueba que inform_bad_format lanza un ParseError si falta una hoja.
    """
    # Configurar un mock para el libro de trabajo de openpyxl que no tiene una hoja.
    mock_workbook = MagicMock()
    mock_workbook.sheetnames = ["Hoja1"]  # Falta Hoja2
    mock_load_workbook.return_value = mock_workbook
    
    # Creamos una instancia con un archivo de Excel falso
    gestor = GestorExcelFileData(
      sheets_columns_configuration=self.sheets_config,
      gestor_sheet=MagicMock(),
      file_xls=self.file_path
    )

    with self.assertRaises(ParseError) as context:
      gestor.inform_bad_format()

    expected_message = 'No se pudo realizar la carga debido a que el formato no es correcto por la falta de la hoja "Hoja2" en el archivo Excel.\nPor favor utilice un formato válido.'
    self.assertEqual(str(context.exception), expected_message)
      
  @patch('openpyxl.load_workbook')
  def test_inform_bad_format_passes_with_correct_sheets(self, mock_load_workbook):
    """
    Prueba que inform_bad_format no lanza un error si las hojas existen.
    """
    mock_workbook = MagicMock()
    mock_workbook.sheetnames = ["Hoja1", "Hoja2"]
    mock_load_workbook.return_value = mock_workbook

    gestor = GestorExcelFileData(
      sheets_columns_configuration=self.sheets_config,
      gestor_sheet=MagicMock(),
      file_xls=self.file_path
    )
    
    # No debería levantar ninguna excepción
    try:
      gestor.inform_bad_format()
    except ParseError:
      self.fail("inform_bad_format levantó un ParseError inesperadamente")

  # --- Pruebas para el método get_data_from_file ---

  @patch('openpyxl.load_workbook')
  def test_get_data_from_file_extracts_data_correctly(self, mock_load_workbook):
    """
    Prueba que get_data_from_file extrae datos de todas las hojas correctamente.
    """
    # 1. Mockeamos la dependencia de GestorExcelFileData
    # Simulamos una instancia de GestorExcelSheetData
    mock_gestor_sheet = MagicMock()

    # Configuramos lo que get_data_from_sheet debe devolver para cada llamada
    mock_gestor_sheet.get_data_from_sheet.side_effect = [
      [{"row_data_sheet1": "data1"}],
      [{"row_data_sheet2": "data2"}],
    ]

    # 2. Simulamos el libro de trabajo de openpyxl
    # Creamos mocks para las hojas
    mock_sheet1 = MagicMock()
    mock_sheet2 = MagicMock()
    
    # Configuramos el mock del libro de trabajo para que devuelva los mocks de hoja
    mock_workbook = MagicMock()
    mock_workbook.__getitem__.side_effect = {
      "Hoja1": mock_sheet1,
      "Hoja2": mock_sheet2,
    }.get
    
    # Le decimos al patch qué devolver cuando se llame a load_workbook
    mock_load_workbook.return_value = mock_workbook

    # 3. Creamos la instancia del objeto a probar
    gestor = GestorExcelFileData(
      sheets_columns_configuration=self.sheets_config,
      gestor_sheet=mock_gestor_sheet,
      file_xls=self.file_path
    )

    # 4. Ejecutamos la prueba
    result = gestor.get_data_from_file()

    # 5. Verificamos que los datos devueltos sean correctos
    expected_result = {
      "Hoja1:Datos": [{"row_data_sheet1": "data1"}],
      "Hoja2:Info": [{"row_data_sheet2": "data2"}],
    }
    self.assertEqual(result, expected_result)
    
    # 6. Verificamos que los métodos del mock fueron llamados correctamente
    mock_gestor_sheet.get_data_from_sheet.assert_any_call(
      column_ubication={"col1": "A", "col2": "B"}, sheet=mock_sheet1
    )
    mock_gestor_sheet.get_data_from_sheet.assert_any_call(
      column_ubication={"col3": "C", "col4": "D"}, sheet=mock_sheet2
    )
    
    # Es una buena práctica verificar también el número total de llamadas
    self.assertEqual(mock_gestor_sheet.get_data_from_sheet.call_count, 2)
    
    # Y que el libro de trabajo se cerró correctamente
    mock_workbook.close.assert_called_once()

  def test_get_data_from_file_handles_exception_gracefully(self):
    """
    Prueba que get_data_from_file maneja excepciones internas sin propagarlas.
    """
    # Configuramos un mock para `get_data_from_sheet` que lanza una excepción
    mock_gestor_sheet = MagicMock(spec=GestorExcelSheetData)
    mock_gestor_sheet.get_data_from_sheet.side_effect = Exception("Simulated read error")
    
    # No es necesario mockear `openpyxl.load_workbook` porque el error ocurre después.
    gestor = GestorExcelFileData(
      sheets_columns_configuration=self.sheets_config,
      gestor_sheet=mock_gestor_sheet,
      file_xls=self.file_path
    )
    
    # La función debería capturar la excepción y devolver None
    # O dependiendo de la lógica, podría devolver un diccionario vacío.
    # En tu código actual, `get_data_from_file` devuelve `None` en caso de excepción.
    result = gestor.get_data_from_file()
    self.assertIsNone(result)