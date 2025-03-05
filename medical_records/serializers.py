from rest_framework import serializers
from .models import *

class PatientDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = PatientData
    fields = '__all__'

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