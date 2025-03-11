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
  collision = CollisionSerializer(required=False, many=True)
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

  def create(self, validated_data):
    healthcare_record_data = validated_data.pop("healthcare_record", None)
    injury_record_data = validated_data.pop("injury_record", None)
    collision_data = validated_data.pop("collision", [])
    drug_abuse_data = validated_data.pop("drug_abuse", [])
    vital_sign_gcs_qualifier_data = validated_data.pop("vital_sign_gcs_qualifier", [])
    hospitalization_variable_data = validated_data.pop("hospitalization_variable", [])
    hospitalization_complication_data = validated_data.pop("hospitalization_complication", [])
    trauma_register_icd10_data = validated_data.pop("trauma_register_icd10", [])
    intensive_care_unit_data = validated_data.pop("intensive_care_unit", [])
    imaging_data = validated_data.pop("imaging", [])
    apparent_intent_injury_data = validated_data.pop("apparent_intent_injury", [])
    burn_injury_data = validated_data.pop("burn_injury", [])
    firearm_injury_data = validated_data.pop("firearm_injury", [])
    penetrating_injury_data = validated_data.pop("penetrating_injury", [])
    poisoning_injury_data = validated_data.pop("poisoning_injury", [])
    violence_injury_data = validated_data.pop("violence_injury", [])
    device_data = validated_data.pop("device", [])
    laboratory_data = validated_data.pop("laboratory", [])
    physical_exam_body_part_injury_data = validated_data.pop("physical_exam_body_part_injury", [])
    procedure_data = validated_data.pop("procedure", [])
    prehospital_procedure_data = validated_data.pop("prehospital_procedure", [])
    transportation_mode_data = validated_data.pop("transportation_mode", [])
    vital_sign_data = validated_data.pop("vital_sign", [])
    
    patient = PatientData.objects.create(**validated_data)
    
    if (healthcare_record_data):
      HealthcareRecord.objects.create(trauma_register_record_id=patient, **healthcare_record_data)
    
    if (injury_record_data):
      InjuryRecord.objects.create(trauma_register_record_id=patient, **injury_record_data)

    for collision in collision_data:
      Collision.objects.create(trauma_register_record_id=patient, **collision)
    
    for drug_abuse in drug_abuse_data: 
      DrugAbuse.objects.create(trauma_register_record_id=patient, **drug_abuse)

    for vital_sign_gcs_qualifier in vital_sign_gcs_qualifier_data: 
      VitalSignGcsQualifier.objects.create(trauma_register_record_id=patient, **vital_sign_gcs_qualifier)

    for hospitalization_variable in hospitalization_variable_data: 
      HospitalizationVariable.objects.create(trauma_register_record_id=patient, **hospitalization_variable)

    for hospitalization_complication in hospitalization_complication_data: 
      HospitalizationComplication.objects.create(trauma_register_record_id=patient, **hospitalization_complication)

    for trauma_register_icd10 in trauma_register_icd10_data: 
      TraumaRegisterIcd10.objects.create(trauma_register_record_id=patient, **trauma_register_icd10)

    for intensive_care_unit in intensive_care_unit_data: 
      IntensiveCareUnit.objects.create(trauma_register_record_id=patient, **intensive_care_unit)

    for imaging in imaging_data: 
      Imaging.objects.create(trauma_register_record_id=patient, **imaging)

    for apparent_intent_injury in apparent_intent_injury_data: 
      ApparentIntentInjury.objects.create(trauma_register_record_id=patient, **apparent_intent_injury)

    for burn_injury in burn_injury_data: 
      BurnInjury.objects.create(trauma_register_record_id=patient, **burn_injury)

    for firearm_injury in firearm_injury_data: 
      FirearmInjury.objects.create(trauma_register_record_id=patient, **firearm_injury)

    for penetrating_injury in penetrating_injury_data: 
      PenetratingInjury.objects.create(trauma_register_record_id=patient, **penetrating_injury)

    for poisoning_injury in poisoning_injury_data: 
      PoisoningInjury.objects.create(trauma_register_record_id=patient, **poisoning_injury)

    for violence_injury in violence_injury_data: 
      ViolenceInjury.objects.create(trauma_register_record_id=patient, **violence_injury)

    for device in device_data: 
      Device.objects.create(trauma_register_record_id=patient, **device)

    for laboratory in laboratory_data: 
      Laboratory.objects.create(trauma_register_record_id=patient, **laboratory)

    for physical_exam_body_part_injury in physical_exam_body_part_injury_data: 
      PhysicalExamBodyPartInjury.objects.create(trauma_register_record_id=patient, **physical_exam_body_part_injury)

    for procedure in procedure_data: 
      Procedure.objects.create(trauma_register_record_id=patient, **procedure)

    for prehospital_procedure in prehospital_procedure_data: 
      PrehospitalProcedure.objects.create(trauma_register_record_id=patient, **prehospital_procedure)

    for transportation_mode in transportation_mode_data: 
      TransportationMode.objects.create(trauma_register_record_id=patient, **transportation_mode)

    for vital_sign in vital_sign_data: 
      VitalSign.objects.create(trauma_register_record_id=patient, **vital_sign)
    
    return patient 
