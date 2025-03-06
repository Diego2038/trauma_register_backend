from rest_framework import serializers
from .models import *

class HealthcareRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = HealthcareRecord
    fields = '__all__'

class InjuryRecordSerializer(serializers.ModelSerializer):
  class Meta:
    model = InjuryRecord
    fields = '__all__'

class CollisionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collision
    fields = '__all__'

class DrugAbuseSerializer(serializers.ModelSerializer):
  class Meta:
    model = DrugAbuse
    fields = '__all__'

class VitalSignGcsQualifierSerializer(serializers.ModelSerializer):
  class Meta:
    model = VitalSignGcsQualifier
    fields = '__all__'

class HospitalizationVariableSerializer(serializers.ModelSerializer):
  class Meta:
    model = HospitalizationVariable
    fields = '__all__'

class HospitalizationComplicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = HospitalizationComplication
    fields = '__all__'

class TraumaRegisterIcd10Serializer(serializers.ModelSerializer):
  class Meta:
    model = TraumaRegisterIcd10
    fields = '__all__'

class IntensiveCareUnitSerializer(serializers.ModelSerializer):
  class Meta:
    model = IntensiveCareUnit
    fields = '__all__'

class ImagingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Imaging
    fields = '__all__'

class ApparentIntentInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = ApparentIntentInjury
    fields = '__all__'

class BurnInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = BurnInjury
    fields = '__all__'

class FirearmInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = FirearmInjury
    fields = '__all__'

class PenetratingInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = PenetratingInjury
    fields = '__all__'

class PoisoningInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = PoisoningInjury
    fields = '__all__'

class ViolenceInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = ViolenceInjury
    fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Laboratory
    fields = '__all__'

class PhysicalExamBodyPartInjurySerializer(serializers.ModelSerializer):
  class Meta:
    model = PhysicalExamBodyPartInjury
    fields = '__all__'

class ProcedureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Procedure
    fields = '__all__'

class PrehospitalProcedureSerializer(serializers.ModelSerializer):
  class Meta:
    model = PrehospitalProcedure
    fields = '__all__'

class TransportationModeSerializer(serializers.ModelSerializer):
  class Meta:
    model = TransportationMode
    fields = '__all__'

class VitalSignSerializer(serializers.ModelSerializer):
  class Meta:
    model = VitalSign
    fields = '__all__'

class PatientDataSerializer(serializers.ModelSerializer):
  healthcare_record = HealthcareRecordSerializer(required=False)
  injury_record = InjuryRecordSerializer(required=False)
  collision = CollisionSerializer(many=True, required=False)
  drug_abuse = DrugAbuseSerializer(required=False, many=True)
  vital_sign_gcs_qualifier = VitalSignGcsQualifierSerializer(required=False, many=True)
  hospitalization_variable = HospitalizationVariableSerializer(required=False, many=True)
  hospitalization_complication = HospitalizationComplicationSerializer(required=False, many=True)
  trauma_register_icd10 = TraumaRegisterIcd10Serializer(required=False, many=True)
  intensive_care_unit = IntensiveCareUnitSerializer(required=False, many=True)
  imaging = ImagingSerializer(required=False, many=True)
  apparent_intent_injury = ApparentIntentInjurySerializer(required=False, many=True)
  burn_injury = BurnInjurySerializer(required=False, many=True)
  firearm_injury = FirearmInjurySerializer(required=False, many=True)
  penetrating_injury = PenetratingInjurySerializer(required=False, many=True)
  poisoning_injury = PoisoningInjurySerializer(required=False, many=True)
  violence_injury = ViolenceInjurySerializer(required=False, many=True)
  device = DeviceSerializer(required=False, many=True)
  laboratory = LaboratorySerializer(required=False, many=True)
  physical_exam_body_part_injury = PhysicalExamBodyPartInjurySerializer(required=False, many=True)
  procedure = ProcedureSerializer(required=False, many=True)
  prehospital_procedure = PrehospitalProcedureSerializer(required=False, many=True)
  transportation_mode = TransportationModeSerializer(required=False, many=True)
  vital_sign = VitalSignSerializer(required=False, many=True)
  
  class Meta:
    model = PatientData
    fields = '__all__'