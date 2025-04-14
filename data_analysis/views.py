from django.db.models import Count, Q, Exists, OuterRef, F, ExpressionWrapper, IntegerField, Value, Case, When, FloatField
from django.db.models.functions import Cast
from django.utils.timezone import now
from medical_records.models import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class AmountOfPatientDataStatsViewSet(ViewSet):
  def list(self, request):
    total = PatientData.objects.count()
    return Response({"total": total})

class PatientGenderStatsViewSet(ViewSet):
  def list(self, request):
    gender_counts = (
      PatientData.objects
      .values("genero")  # Agrupa por "genero"
      .annotate(total=Count("trauma_register_record_id"))  # Cuenta la cantidad de registros, se usa el id para que cuente también los valores nulos
    )

    # Convertimos valores NULL en "No registra"
    formatted_data = [
      {
        'genero': item["genero"] if item["genero"] is not None else "No registra", 
        'total': item["total"]
      } for item in gender_counts
    ]

    return Response({"data": formatted_data})

class PatientAgeStatsViewSet(ViewSet):
   def list(self, request):
    # Anotamos la edad en años para todos los pacientes
    patients = PatientData.objects.annotate(
      edad_en_anios=Case(
        When(unidad_de_edad="Años", then=F("edad")),
        When(edad__isnull=False, then=F("edad") / Value(12.0)),
        default=None,
        output_field=FloatField(),
      )
    )

    # Inicializar los rangos
    age_ranges = {
      "0-10": 0,
      "11-20": 0,
      "21-30": 0,
      "31-40": 0,
      "41-50": 0,
      "51-60": 0,
      "61-70": 0,
      "71-80": 0,
      "81-90": 0,
      "91-100": 0,
      "100+": 0,
      "-1": 0,
    }

    for p in patients:
      edad = p.edad_en_anios

      if edad is None:
        age_ranges["-1"] += 1
      elif 0 <= edad <= 10:
        age_ranges["0-10"] += 1
      elif 11 <= edad <= 20:
        age_ranges["11-20"] += 1
      elif 21 <= edad <= 30:
        age_ranges["21-30"] += 1
      elif 31 <= edad <= 40:
        age_ranges["31-40"] += 1
      elif 41 <= edad <= 50:
        age_ranges["41-50"] += 1
      elif 51 <= edad <= 60:
        age_ranges["51-60"] += 1
      elif 61 <= edad <= 70:
        age_ranges["61-70"] += 1
      elif 71 <= edad <= 80:
        age_ranges["71-80"] += 1
      elif 81 <= edad <= 90:
        age_ranges["81-90"] += 1
      elif 91 <= edad <= 100:
        age_ranges["91-100"] += 1
      elif edad > 100:
        age_ranges["100+"] += 1
      else:
        age_ranges["-1"] += 1

    formatted_data = [
      {
        "rango_edad": rango, "total": total
      } for rango, total in age_ranges.items()
    ]

    return Response({"data": formatted_data})
  
# class PatientDataWithRelationsStatsViewSet(ViewSet):
#   def list(self, request):
#     patient_counts = (
#       PatientData.objects
#       .annotate(
#           has_collision=Count("collision", filter=Q(collision__isnull=False), distinct=True),
#           has_drug_abuse=Count("drug_abuse", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_vital_sign_gcs_qualifier=Count("vital_sign_gcs_qualifier", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_hospitalization_variable=Count("hospitalization_variable", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_hospitalization_complication=Count("hospitalization_complication", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_trauma_register_icd10=Count("trauma_register_icd10", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_intensive_care_unit=Count("intensive_care_unit", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_imaging=Count("imaging", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_apparent_intent_injury=Count("apparent_intent_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_burn_injury=Count("burn_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_firearm_injury=Count("firearm_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_penetrating_injury=Count("penetrating_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_poisoning_injury=Count("poisoning_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_violence_injury=Count("violence_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_device=Count("device", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_laboratory=Count("laboratory", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_physical_exam_body_part_injury=Count("physical_exam_body_part_injury", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_procedure=Count("procedure", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_prehospital_procedure=Count("prehospital_procedure", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_transportation_mode=Count("transportation_mode", filter=Q(drug_abuse__isnull=False), distinct=True),
#           has_vital_sign=Count("vital_sign", filter=Q(drug_abuse__isnull=False), distinct=True),
#       )
#       .aggregate(
#           total_with_collision=Count("trauma_register_record_id", filter=Q(has_collision__gt=0), distinct=True),
#           total_with_drug_abuse=Count("trauma_register_record_id", filter=Q(has_drug_abuse__gt=0), distinct=True),
#           total_with_vital_sign_gcs_qualifier=Count("trauma_register_record_id", filter=Q(has_vital_sign_gcs_qualifier__gt=0), distinct=True),
#           total_with_hospitalization_variable=Count("trauma_register_record_id", filter=Q(has_hospitalization_variable__gt=0), distinct=True),
#           total_with_hospitalization_complication=Count("trauma_register_record_id", filter=Q(has_hospitalization_complication__gt=0), distinct=True),
#           total_with_trauma_register_icd10=Count("trauma_register_record_id", filter=Q(has_trauma_register_icd10__gt=0), distinct=True),
#           total_with_intensive_care_unit=Count("trauma_register_record_id", filter=Q(has_intensive_care_unit__gt=0), distinct=True),
#           total_with_imaging=Count("trauma_register_record_id", filter=Q(has_imaging__gt=0), distinct=True),
#           total_with_apparent_intent_injury=Count("trauma_register_record_id", filter=Q(has_apparent_intent_injury__gt=0), distinct=True),
#           total_with_burn_injury=Count("trauma_register_record_id", filter=Q(has_burn_injury__gt=0), distinct=True),
#           total_with_firearm_injury=Count("trauma_register_record_id", filter=Q(has_firearm_injury__gt=0), distinct=True),
#           total_with_penetrating_injury=Count("trauma_register_record_id", filter=Q(has_penetrating_injury__gt=0), distinct=True),
#           total_with_poisoning_injury=Count("trauma_register_record_id", filter=Q(has_poisoning_injury__gt=0), distinct=True),
#           total_with_violence_injury=Count("trauma_register_record_id", filter=Q(has_violence_injury__gt=0), distinct=True),
#           total_with_device=Count("trauma_register_record_id", filter=Q(has_device__gt=0), distinct=True),
#           total_with_laboratory=Count("trauma_register_record_id", filter=Q(has_laboratory__gt=0), distinct=True),
#           total_with_physical_exam_body_part_injury=Count("trauma_register_record_id", filter=Q(has_physical_exam_body_part_injury__gt=0), distinct=True),
#           total_with_procedure=Count("trauma_register_record_id", filter=Q(has_procedure__gt=0), distinct=True),
#           total_with_prehospital_procedure=Count("trauma_register_record_id", filter=Q(has_prehospital_procedure__gt=0), distinct=True),
#           total_with_transportation_mode=Count("trauma_register_record_id", filter=Q(has_transportation_mode__gt=0), distinct=True),
#           total_with_vital_sign=Count("trauma_register_record_id", filter=Q(has_vital_sign__gt=0), distinct=True),
#       )
#     )

#     return Response({"data": patient_counts})

class PatientDataWithRelationsStatsViewSet(ViewSet):
    def list(self, request):
        patient_counts = (
            PatientData.objects
            .annotate(
                has_collision=Exists(Collision.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_drug_abuse=Exists(DrugAbuse.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_vital_sign_gcs_qualifier=Exists(VitalSignGcsQualifier.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_hospitalization_variable=Exists(HospitalizationVariable.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_hospitalization_complication=Exists(HospitalizationComplication.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_trauma_register_icd10=Exists(TraumaRegisterIcd10.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_intensive_care_unit=Exists(IntensiveCareUnit.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_imaging=Exists(Imaging.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_apparent_intent_injury=Exists(ApparentIntentInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_burn_injury=Exists(BurnInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_firearm_injury=Exists(FirearmInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_penetrating_injury=Exists(PenetratingInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_poisoning_injury=Exists(PoisoningInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_violence_injury=Exists(ViolenceInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_device=Exists(Device.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_laboratory=Exists(Laboratory.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_physical_exam_body_part_injury=Exists(PhysicalExamBodyPartInjury.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_procedure=Exists(Procedure.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_prehospital_procedure=Exists(PrehospitalProcedure.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_transportation_mode=Exists(TransportationMode.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                has_vital_sign=Exists(VitalSign.objects.filter(trauma_register_record_id=OuterRef("trauma_register_record_id"))),
                
                # Agrega las demás relaciones aquí
            )
            .aggregate(
                total_with_collision=Count("trauma_register_record_id", filter=Q(has_collision=True), distinct=True),
                total_with_drug_abuse=Count("trauma_register_record_id", filter=Q(has_drug_abuse=True), distinct=True),
                total_with_vital_sign_gcs_qualifier=Count("trauma_register_record_id", filter=Q(has_vital_sign_gcs_qualifier__gt=0), distinct=True),
                total_with_hospitalization_variable=Count("trauma_register_record_id", filter=Q(has_hospitalization_variable__gt=0), distinct=True),
                total_with_hospitalization_complication=Count("trauma_register_record_id", filter=Q(has_hospitalization_complication__gt=0), distinct=True),
                total_with_trauma_register_icd10=Count("trauma_register_record_id", filter=Q(has_trauma_register_icd10__gt=0), distinct=True),
                total_with_intensive_care_unit=Count("trauma_register_record_id", filter=Q(has_intensive_care_unit__gt=0), distinct=True),
                total_with_imaging=Count("trauma_register_record_id", filter=Q(has_imaging__gt=0), distinct=True),
                total_with_apparent_intent_injury=Count("trauma_register_record_id", filter=Q(has_apparent_intent_injury__gt=0), distinct=True),
                total_with_burn_injury=Count("trauma_register_record_id", filter=Q(has_burn_injury__gt=0), distinct=True),
                total_with_firearm_injury=Count("trauma_register_record_id", filter=Q(has_firearm_injury__gt=0), distinct=True),
                total_with_penetrating_injury=Count("trauma_register_record_id", filter=Q(has_penetrating_injury__gt=0), distinct=True),
                total_with_poisoning_injury=Count("trauma_register_record_id", filter=Q(has_poisoning_injury__gt=0), distinct=True),
                total_with_violence_injury=Count("trauma_register_record_id", filter=Q(has_violence_injury__gt=0), distinct=True),
                total_with_device=Count("trauma_register_record_id", filter=Q(has_device__gt=0), distinct=True),
                total_with_laboratory=Count("trauma_register_record_id", filter=Q(has_laboratory__gt=0), distinct=True),
                total_with_physical_exam_body_part_injury=Count("trauma_register_record_id", filter=Q(has_physical_exam_body_part_injury__gt=0), distinct=True),
                total_with_procedure=Count("trauma_register_record_id", filter=Q(has_procedure__gt=0), distinct=True),
                total_with_prehospital_procedure=Count("trauma_register_record_id", filter=Q(has_prehospital_procedure__gt=0), distinct=True),
                total_with_transportation_mode=Count("trauma_register_record_id", filter=Q(has_transportation_mode__gt=0), distinct=True),
                total_with_vital_sign=Count("trauma_register_record_id", filter=Q(has_vital_sign__gt=0), distinct=True),
                
                # Agrega las demás relaciones aquí 
            )
        )
        
        data = {
          "Colisión": patient_counts["total_with_collision"],
          "Abuso de drogas": patient_counts["total_with_drug_abuse"],
          "Lesión intencional aparente": patient_counts["total_with_apparent_intent_injury"],
          "Lesión por quemadura": patient_counts["total_with_burn_injury"],
          "Lesión penetrante": patient_counts["total_with_penetrating_injury"],
          "Lesión por arma de fuego": patient_counts["total_with_firearm_injury"],
          "Lesión por envenenamiento": patient_counts["total_with_poisoning_injury"],
          "Lesión violenta": patient_counts["total_with_violence_injury"],
        }

        return Response({"data": data})

class ObtainInsuredPatientsStatsViewSet(ViewSet):
  def list(self, request):
    insured_data = PatientData.objects.aggregate(
      asegurados=Count('healthcare_record', filter=Q(healthcare_record__paciente_asegurado=True)),
      no_asegurados=Count('healthcare_record', filter=Q(healthcare_record__paciente_asegurado=False)),
      no_registra=Count('healthcare_record', filter=Q(healthcare_record__paciente_asegurado=None)),
      sin_informacion=Count('trauma_register_record_id', filter=Q(healthcare_record=None))
    )

    formatted_data = {
      "Asegurados": insured_data['asegurados'],
      "No asegurados": insured_data['no_asegurados'],
      "No registra": insured_data['no_registra'] + insured_data['sin_informacion'],
    }

    return Response({"data": formatted_data})

class TypeOfPatientAdmissionStatsViewSet(ViewSet):
  def list(self, request):
    insured_data = PatientData.objects.aggregate(
      directo=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision='Directo')),
      emergencia=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision='Emergencia')),
      normal=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision='Normal')),
      otra=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision='Otra')),
      urgencia=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision='Urgencia')),
      no_registra=Count('healthcare_record', filter=Q(healthcare_record__tipo_de_admision=None)),
      sin_informacion=Count('trauma_register_record_id', filter=Q(healthcare_record=None))
    )

    formatted_data = {
      "Directo": insured_data['directo'],
      "Emergencia": insured_data['emergencia'],
      "Normal": insured_data['normal'],
      "Otra": insured_data['otra'],
      "Urgencia": insured_data['urgencia'],
      "No registra": insured_data['no_registra'] + insured_data['sin_informacion'],
    }

    return Response({"data": formatted_data})