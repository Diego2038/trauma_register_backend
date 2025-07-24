from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import PatientDataSerializer, HealthcareRecordSerializer, InjuryRecordSerializer, CollisionSerializer, DrugAbuseSerializer, VitalSignGcsQualifierSerializer, HospitalizationVariableSerializer, HospitalizationComplicationSerializer, TraumaRegisterIcd10Serializer, IntensiveCareUnitSerializer, ImagingSerializer, ApparentIntentInjurySerializer, BurnInjurySerializer, FirearmInjurySerializer, PenetratingInjurySerializer, PoisoningInjurySerializer, ViolenceInjurySerializer, DeviceSerializer, LaboratorySerializer, PhysicalExamBodyPartInjurySerializer, ProcedureSerializer, PrehospitalProcedureSerializer, TransportationModeSerializer, VitalSignSerializer
from .models import PatientData, HealthcareRecord, InjuryRecord

class PatientDataViewsets(viewsets.ModelViewSet):
  serializer_class = PatientDataSerializer
  queryset = PatientDataSerializer.Meta.model.objects.all()
  lookup_field = 'trauma_register_record_id'
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Errores del serializer:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  def update(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData,
      trauma_register_record_id=trauma_register_record_id,
    )
    serializer = self.get_serializer(
      patient_data, 
      data=request.data, 
      partial=True
    )
    if serializer.is_valid(raise_exception=True):
      self.perform_update(serializer)
      return Response(serializer.data)
    return Response(serializer.errors)
  
  def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData,
      trauma_register_record_id=trauma_register_record_id,
    )
    patient_data_serializer = PatientDataSerializer(patient_data)
    return Response(patient_data_serializer.data)
  
  def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData, 
      trauma_register_record_id=trauma_register_record_id,
    )
    self.perform_destroy(patient_data)
    return Response(status=status.HTTP_204_NO_CONTENT)

class HealthcareRecordViewsets(viewsets.ModelViewSet):
  serializer_class = HealthcareRecordSerializer
  queryset = HealthcareRecordSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)

class InjuryRecordViewsets(viewsets.ModelViewSet):
  serializer_class = InjuryRecordSerializer
  queryset = InjuryRecordSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class CollisionViewsets(viewsets.ModelViewSet):
  serializer_class = CollisionSerializer
  queryset = CollisionSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class DrugAbuseViewsets(viewsets.ModelViewSet):
  serializer_class = DrugAbuseSerializer
  queryset = DrugAbuseSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class VitalSignGcsQualifierViewsets(viewsets.ModelViewSet):
  serializer_class = VitalSignGcsQualifierSerializer
  queryset = VitalSignGcsQualifierSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class HospitalizationVariableViewsets(viewsets.ModelViewSet):
  serializer_class = HospitalizationVariableSerializer
  queryset = HospitalizationVariableSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class HospitalizationComplicationViewsets(viewsets.ModelViewSet):
  serializer_class = HospitalizationComplicationSerializer
  queryset = HospitalizationComplicationSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class TraumaRegisterIcd10Viewsets(viewsets.ModelViewSet):
  serializer_class = TraumaRegisterIcd10Serializer
  queryset = TraumaRegisterIcd10Serializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class IntensiveCareUnitViewsets(viewsets.ModelViewSet):
  serializer_class = IntensiveCareUnitSerializer
  queryset = IntensiveCareUnitSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class ImagingViewsets(viewsets.ModelViewSet):
  serializer_class = ImagingSerializer
  queryset = ImagingSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class ApparentIntentInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = ApparentIntentInjurySerializer
  queryset = ApparentIntentInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class BurnInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = BurnInjurySerializer
  queryset = BurnInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class FirearmInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = FirearmInjurySerializer
  queryset = FirearmInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class PenetratingInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PenetratingInjurySerializer
  queryset = PenetratingInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class PoisoningInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PoisoningInjurySerializer
  queryset = PoisoningInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class ViolenceInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = ViolenceInjurySerializer
  queryset = ViolenceInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class DeviceViewsets(viewsets.ModelViewSet):
  serializer_class = DeviceSerializer
  queryset = DeviceSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class LaboratoryViewsets(viewsets.ModelViewSet):
  serializer_class = LaboratorySerializer
  queryset = LaboratorySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class PhysicalExamBodyPartInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PhysicalExamBodyPartInjurySerializer
  queryset = PhysicalExamBodyPartInjurySerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class ProcedureViewsets(viewsets.ModelViewSet):
  serializer_class = ProcedureSerializer
  queryset = ProcedureSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class PrehospitalProcedureViewsets(viewsets.ModelViewSet):
  serializer_class = PrehospitalProcedureSerializer
  queryset = PrehospitalProcedureSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class TransportationModeViewsets(viewsets.ModelViewSet):
  serializer_class = TransportationModeSerializer
  queryset = TransportationModeSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
class VitalSignViewsets(viewsets.ModelViewSet):
  serializer_class = VitalSignSerializer
  queryset = VitalSignSerializer.Meta.model.objects.all()
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)

class PatientsIdsSet(ViewSet):
  def list(self, request):
    partial_id = request.data.get("trauma_register_record_id")
    
    if not partial_id:
      return Response({"data": []})
    
    patients_ids = (
      PatientData.objects
      .filter(trauma_register_record_id__icontains=partial_id)
      .values("trauma_register_record_id")
      .distinct()[:5]
    )

    formatted_data = [
      item['trauma_register_record_id'] for item in patients_ids
    ]

    return Response({"data": formatted_data})