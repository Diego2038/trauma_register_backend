from unittest.mock import patch, MagicMock, call
from types import SimpleNamespace
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.request import Request
from rest_framework import status
from datetime import date
from collections import namedtuple

from data_analysis.views import (
  AmountOfPatientDataStatsViewSet,
  PatientGenderStatsViewSet,
  PatientAgeStatsViewSet,
  PatientDataWithRelationsStatsViewSet,
  ObtainInsuredPatientsStatsViewSet,
  TypeOfPatientAdmissionStatsViewSet,
  TraumaCountByDateStatsViewSet,
  FilterRequest
)

# --- Mocks para modelos y datos ---
MockPatientData = namedtuple('MockPatientData', ['trauma_register_record_id', 'genero', 'edad', 'unidad_de_edad'])
MockInjuryRecord = namedtuple('MockInjuryRecord', ['trauma_register_record_id', 'fecha_y_hora_del_evento'])

# --- Pruebas para FilterRequest ---

class FilterRequestTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.PatientData.objects')
  def test_filterPatientDataByEmergencyDate(self, mock_objects):
    # Preparar el mock del queryset
    mock_queryset = MagicMock()
    # Hacemos que filter() devuelva el mismo mock para permitir encadenamiento
    mock_queryset.filter.return_value = mock_queryset
    mock_objects.all.return_value = mock_queryset

    # Requests simulados (solo necesitamos .data)
    req_no_filters = SimpleNamespace(data={})
    req_start_date = SimpleNamespace(data={'start_date': '2023-01-01'})
    req_end_date = SimpleNamespace(data={'end_date': '2023-12-31'})
    req_both_dates = SimpleNamespace(data={'start_date': '2023-01-01', 'end_date': '2023-12-31'})

    # Caso 1: Sin filtros -> debe retornar el queryset inicial
    result_queryset = FilterRequest.filterPatientDataByEmergencyDate(req_no_filters)
    mock_objects.all.assert_called_once()
    self.assertEqual(result_queryset, mock_queryset)

    # Caso 2: Con filtro de inicio -> verificar llamada a filter con fecha de inicio
    _ = FilterRequest.filterPatientDataByEmergencyDate(req_start_date)
    mock_queryset.filter.assert_any_call(
      healthcare_record__fecha_y_hora_de_llegada_del_paciente__isnull=False,
      healthcare_record__fecha_y_hora_de_llegada_del_paciente__date__gte=date(2023, 1, 1)
    )

    # Caso 3: Con filtro de fin -> verificar llamada a filter con fecha de fin
    _ = FilterRequest.filterPatientDataByEmergencyDate(req_end_date)
    mock_queryset.filter.assert_any_call(
      healthcare_record__fecha_y_hora_de_alta__isnull=False,
      healthcare_record__fecha_y_hora_de_alta__date__lte=date(2023, 12, 31)
    )

    # Caso 4: Ambos filtros -> verificar que se llamaron ambas condiciones (en orden)
    # Resetear llamadas previas para una comprobación limpia (opcional)
    mock_queryset.filter.reset_mock()
    mock_objects.all.return_value = mock_queryset

    _ = FilterRequest.filterPatientDataByEmergencyDate(req_both_dates)

    expected_calls = [
      call(
        healthcare_record__fecha_y_hora_de_llegada_del_paciente__isnull=False,
        healthcare_record__fecha_y_hora_de_llegada_del_paciente__date__gte=date(2023, 1, 1)
      ),
      call(
        healthcare_record__fecha_y_hora_de_alta__isnull=False,
        healthcare_record__fecha_y_hora_de_alta__date__lte=date(2023, 12, 31)
      ),
    ]
    mock_queryset.filter.assert_has_calls(expected_calls, any_order=False)
  
  @patch('data_analysis.views.InjuryRecord.objects')
  def test_filterInjuryRecordByEventDate(self, mock_objects):
    # Preparar mock queryset
    mock_queryset = MagicMock()
    mock_queryset.filter.return_value = mock_queryset  # permitir encadenar
    mock_objects.all.return_value = mock_queryset

    # Requests simulados
    req_start_date = SimpleNamespace(data={'start_date': '2023-01-01'})
    req_end_date = SimpleNamespace(data={'end_date': '2023-12-31'})
    req_both_dates = SimpleNamespace(data={'start_date': '2023-01-01', 'end_date': '2023-12-31'})

    # Caso 1: Con filtro de inicio
    _ = FilterRequest.filterInjuryRecordByEventDate(req_start_date)
    mock_queryset.filter.assert_any_call(
      fecha_y_hora_del_evento__isnull=False,
      fecha_y_hora_del_evento__date__gte=date(2023, 1, 1)
    )

    # Caso 2: Con filtro de fin
    mock_queryset.filter.reset_mock()
    _ = FilterRequest.filterInjuryRecordByEventDate(req_end_date)
    mock_queryset.filter.assert_any_call(
      fecha_y_hora_del_evento__isnull=False,
      fecha_y_hora_del_evento__date__lte=date(2023, 12, 31)
    )

    # Caso 3: Con ambos filtros
    mock_queryset.filter.reset_mock()
    _ = FilterRequest.filterInjuryRecordByEventDate(req_both_dates)
    expected_calls = [
      call(
        fecha_y_hora_del_evento__isnull=False,
        fecha_y_hora_del_evento__date__gte=date(2023, 1, 1)
      ),
      call(
        fecha_y_hora_del_evento__isnull=False,
        fecha_y_hora_del_evento__date__lte=date(2023, 12, 31)
      )
    ]
    mock_queryset.filter.assert_has_calls(expected_calls, any_order=False)

# --- Pruebas para ViewSets de Estadísticas ---

class AmountOfPatientDataStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = AmountOfPatientDataStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_total_count(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.count.return_value = 10
    mock_filter.return_value = mock_queryset
    
    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, {"type": 'single_value', "data": 10})
    mock_filter.assert_called_once()
    mock_queryset.count.assert_called_once()

class PatientGenderStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = PatientGenderStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_gender_counts(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.values.return_value.annotate.return_value = [
      {"genero": "M", "total": 5},
      {"genero": "F", "total": 3},
      {"genero": None, "total": 2},
    ]
    mock_filter.return_value = mock_queryset

    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)

    expected_data = [
      {'tag': 'M', 'total': 5},
      {'tag': 'F', 'total': 3},
      {'tag': 'No registra', 'total': 2},
    ]

    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, {"type": 'categorical', "data": expected_data})
    mock_filter.assert_called_once()

class PatientAgeStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = PatientAgeStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_age_range_counts(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.annotate.return_value = [
      MagicMock(edad_en_anios=25),
      MagicMock(edad_en_anios=15),
      MagicMock(edad_en_anios=5),
      MagicMock(edad_en_anios=1.25),
      MagicMock(edad_en_anios=65),
      MagicMock(edad_en_anios=110),
      MagicMock(edad_en_anios=None),
    ]
    mock_filter.return_value = mock_queryset
    
    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data_dict = {
      "0-10": 2, # El de 5 años y el de 1.25 años
      "11-20": 1,
      "21-30": 1,
      "31-40": 0,
      "41-50": 0,
      "51-60": 0,
      "61-70": 1,
      "71-80": 0,
      "81-90": 0,
      "91-100": 0,
      "100+": 1,
      "N/A": 1,
    }

    response_data_dict = {item['tag']: item['total'] for item in response.data['data']}
    self.assertEqual(response_data_dict, expected_data_dict)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class PatientDataWithRelationsStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = PatientDataWithRelationsStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_relation_counts(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.annotate.return_value.aggregate.return_value = {
      'total_with_collision': 5,
      'total_with_drug_abuse': 3,
      'total_with_vital_sign_gcs_qualifier': 1,
      'total_with_hospitalization_variable': 0,
      'total_with_hospitalization_complication': 1,
      'total_with_trauma_register_icd10': 0,
      'total_with_intensive_care_unit': 2,
      'total_with_imaging': 0,
      'total_with_apparent_intent_injury': 1,
      'total_with_burn_injury': 0,
      'total_with_firearm_injury': 2,
      'total_with_penetrating_injury': 1,
      'total_with_poisoning_injury': 0,
      'total_with_violence_injury': 1,
      'total_with_device': 0,
      'total_with_laboratory': 3,
      'total_with_physical_exam_body_part_injury': 0,
      'total_with_procedure': 1,
      'total_with_prehospital_procedure': 0,
      'total_with_transportation_mode': 1,
      'total_with_vital_sign': 0,
    }
    mock_filter.return_value = mock_queryset
    
    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['type'], 'categorical')

class ObtainInsuredPatientsStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = ObtainInsuredPatientsStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_insured_counts(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.aggregate.return_value = {
      'asegurados': 10,
      'no_asegurados': 5,
      'no_registra': 2,
      'sin_informacion': 3,
    }
    mock_filter.return_value = mock_queryset
    
    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data = [
      {'tag': 'Asegurados', 'total': 10},
      {'tag': 'No asegurados', 'total': 5},
      {'tag': 'No registra', 'total': 5}, # 2 + 3 = 5
    ]
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['data'], expected_data)

class TypeOfPatientAdmissionStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = TypeOfPatientAdmissionStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterPatientDataByEmergencyDate')
  def test_update_returns_admission_type_counts(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.aggregate.return_value = {
      'directo': 2,
      'emergencia': 4,
      'normal': 1,
      'otra': 0,
      'urgencia': 3,
      'no_registra': 2,
      'sin_informacion': 1,
    }
    mock_filter.return_value = mock_queryset
    
    request = self.factory.put("/", {})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data = [
      {'tag': 'Directo', 'total': 2},
      {'tag': 'Emergencia', 'total': 4},
      {'tag': 'Normal', 'total': 1},
      {'tag': 'Otra', 'total': 0},
      {'tag': 'Urgencia', 'total': 3},
      {'tag': 'No registra', 'total': 3}, # 2 + 1 = 3
    ]
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['data'], expected_data)

class TraumaCountByDateStatsViewSetTest(TestCase):
  def setUp(self):
    self.factory = APIRequestFactory()
    self.view = TraumaCountByDateStatsViewSet.as_view({"put": "update"})
    User = get_user_model()
    self.user = User.objects.create_user(username="testuser", password="12345", email="test@example.com")

  @patch('data_analysis.views.FilterRequest.filterInjuryRecordByEventDate')
  def test_update_returns_time_series_by_year(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.annotate.return_value.values.return_value.annotate.return_value.order_by.return_value = [
      {'fecha_evento': date(2022, 1, 1), 'total': 5},
      {'fecha_evento': date(2023, 1, 1), 'total': 10},
    ]
    mock_filter.return_value = mock_queryset

    request = self.factory.put("/", {"granularity": "year"})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data = [
      {'date': '2022', 'count': 5},
      {'date': '2023', 'count': 10},
    ]
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['type'], 'time_serie')
    self.assertEqual(response.data['data'], expected_data)

  @patch('data_analysis.views.FilterRequest.filterInjuryRecordByEventDate')
  def test_update_returns_time_series_by_month(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.annotate.return_value.values.return_value.annotate.return_value.order_by.return_value = [
      {'fecha_evento': date(2023, 1, 1), 'total': 5},
      {'fecha_evento': date(2023, 2, 1), 'total': 10},
    ]
    mock_filter.return_value = mock_queryset

    request = self.factory.put("/", {"granularity": "month"})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data = [
      {'date': '2023', 'count': 5},
      {'date': '2023', 'count': 10},
    ]
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['data'], expected_data)

  @patch('data_analysis.views.FilterRequest.filterInjuryRecordByEventDate')
  def test_update_returns_time_series_by_day(self, mock_filter):
    mock_queryset = MagicMock()
    mock_queryset.annotate.return_value.values.return_value.annotate.return_value.order_by.return_value = [
      {'fecha_evento': date(2023, 1, 1), 'total': 5},
      {'fecha_evento': date(2023, 1, 2), 'total': 10},
    ]
    mock_filter.return_value = mock_queryset

    request = self.factory.put("/", {"granularity": "day"})
    force_authenticate(request, user=self.user)
    response = self.view(request)
    
    expected_data = [
      {'date': '2023', 'count': 5},
      {'date': '2023', 'count': 10},
    ]
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['data'], expected_data)
        