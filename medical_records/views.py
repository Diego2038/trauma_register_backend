from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PatientDataSerializer, HealthcareRecordSerializer, InjuryRecordSerializer, CollisionSerializer, DrugAbuseSerializer, VitalSignGcsQualifierSerializer, HospitalizationVariableSerializer, HospitalizationComplicationSerializer, TraumaRegisterIcd10Serializer, IntensiveCareUnitSerializer, ImagingSerializer, ApparentIntentInjurySerializer, BurnInjurySerializer, FirearmInjurySerializer, PenetratingInjurySerializer, PoisoningInjurySerializer, ViolenceInjurySerializer, DeviceSerializer, LaboratorySerializer, PhysicalExamBodyPartInjurySerializer, ProcedureSerializer, PrehospitalProcedureSerializer, TransportationModeSerializer, VitalSignSerializer
from .models import PatientData, HealthcareRecord, InjuryRecord, Collision, DrugAbuse, VitalSignGcsQualifier, HospitalizationVariable, HospitalizationComplication, TraumaRegisterIcd10, IntensiveCareUnit, Imaging, ApparentIntentInjury, BurnInjury, FirearmInjury, PenetratingInjury, PoisoningInjury, ViolenceInjury, Device, Laboratory, PhysicalExamBodyPartInjury, Procedure, PrehospitalProcedure, TransportationMode, VitalSign

class PatientDataViewsets(viewsets.ModelViewSet):
  serializer_class = PatientDataSerializer
  queryset = PatientDataSerializer.Meta.model.objects.all()
  lookup_field = 'trauma_register_record_id'
  
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
  lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  def update(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData,
      trauma_register_record_id=trauma_register_record_id,
    )
    data = get_object_or_404(
      HealthcareRecord,
      trauma_register_record_id=patient_data,
    )
    serializer = self.get_serializer(
      data, 
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
    data = get_object_or_404(
      HealthcareRecord,
      trauma_register_record_id=patient_data,
    )
    serializer = HealthcareRecordSerializer(data)
    return Response(serializer.data)
  
  def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData, 
      trauma_register_record_id=trauma_register_record_id,
    )
    data = get_object_or_404(
      HealthcareRecord,
      trauma_register_record_id=patient_data,
    )
    self.perform_destroy(data)
    return Response(status=status.HTTP_204_NO_CONTENT)

#! Cuidado, experimental

class InjuryRecordViewsets(viewsets.ModelViewSet):
  serializer_class = InjuryRecordSerializer
  queryset = InjuryRecordSerializer.Meta.model.objects.all()
  lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  def update(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData,
      trauma_register_record_id=trauma_register_record_id,
    )
    data = get_object_or_404(
      InjuryRecord,
      trauma_register_record_id=patient_data,
    )
    serializer = self.get_serializer(
      data, 
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
    data = get_object_or_404(
      InjuryRecord,
      trauma_register_record_id=patient_data,
    )
    serializer = InjuryRecordSerializer(data)
    return Response(serializer.data)
  
  def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
    patient_data = get_object_or_404(
      PatientData, 
      trauma_register_record_id=trauma_register_record_id,
    )
    data = get_object_or_404(
      InjuryRecord,
      trauma_register_record_id=patient_data,
    )
    self.perform_destroy(data)
    return Response(status=status.HTTP_204_NO_CONTENT)
  

#! 2
class CollisionViewsets(viewsets.ModelViewSet):
  serializer_class = CollisionSerializer
  queryset = CollisionSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Collision,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Collision,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = CollisionSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Collision,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 3 
class DrugAbuseViewsets(viewsets.ModelViewSet):
  serializer_class = DrugAbuseSerializer
  queryset = DrugAbuseSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     DrugAbuse,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     DrugAbuse,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = DrugAbuseSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     DrugAbuse,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)


#! 4
class VitalSignGcsQualifierViewsets(viewsets.ModelViewSet):
  serializer_class = VitalSignGcsQualifierSerializer
  queryset = VitalSignGcsQualifierSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSignGcsQualifier,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSignGcsQualifier,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = VitalSignGcsQualifierSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSignGcsQualifier,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 5
class HospitalizationVariableViewsets(viewsets.ModelViewSet):
  serializer_class = HospitalizationVariableSerializer
  queryset = HospitalizationVariableSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationVariable,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationVariable,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = HospitalizationVariableSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationVariable,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 6
class HospitalizationComplicationViewsets(viewsets.ModelViewSet):
  serializer_class = HospitalizationComplicationSerializer
  queryset = HospitalizationComplicationSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationComplication,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationComplication,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = HospitalizationComplicationSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     HospitalizationComplication,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 7
class TraumaRegisterIcd10Viewsets(viewsets.ModelViewSet):
  serializer_class = TraumaRegisterIcd10Serializer
  queryset = TraumaRegisterIcd10Serializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TraumaRegisterIcd10,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TraumaRegisterIcd10,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = TraumaRegisterIcd10Serializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TraumaRegisterIcd10,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 8
class IntensiveCareUnitViewsets(viewsets.ModelViewSet):
  serializer_class = IntensiveCareUnitSerializer
  queryset = IntensiveCareUnitSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     IntensiveCareUnit,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     IntensiveCareUnit,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = IntensiveCareUnitSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     IntensiveCareUnit,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 9
class ImagingViewsets(viewsets.ModelViewSet):
  serializer_class = ImagingSerializer
  queryset = ImagingSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Imaging,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Imaging,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = ImagingSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Imaging,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 10
class ApparentIntentInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = ApparentIntentInjurySerializer
  queryset = ApparentIntentInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ApparentIntentInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ApparentIntentInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = ApparentIntentInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ApparentIntentInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 11
class BurnInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = BurnInjurySerializer
  queryset = BurnInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     BurnInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     BurnInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = BurnInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     BurnInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 12
class FirearmInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = FirearmInjurySerializer
  queryset = FirearmInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     FirearmInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     FirearmInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = FirearmInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     FirearmInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 13
class PenetratingInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PenetratingInjurySerializer
  queryset = PenetratingInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PenetratingInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PenetratingInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = PenetratingInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PenetratingInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 14
class PoisoningInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PoisoningInjurySerializer
  queryset = PoisoningInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PoisoningInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PoisoningInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = PoisoningInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PoisoningInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 15
class ViolenceInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = ViolenceInjurySerializer
  queryset = ViolenceInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ViolenceInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ViolenceInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = ViolenceInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     ViolenceInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)
  
#! 16
class DeviceViewsets(viewsets.ModelViewSet):
  serializer_class = DeviceSerializer
  queryset = DeviceSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Device,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Device,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = DeviceSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Device,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 17
class LaboratoryViewsets(viewsets.ModelViewSet):
  serializer_class = LaboratorySerializer
  queryset = LaboratorySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Laboratory,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Laboratory,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = LaboratorySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Laboratory,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 18
class PhysicalExamBodyPartInjuryViewsets(viewsets.ModelViewSet):
  serializer_class = PhysicalExamBodyPartInjurySerializer
  queryset = PhysicalExamBodyPartInjurySerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PhysicalExamBodyPartInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PhysicalExamBodyPartInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = PhysicalExamBodyPartInjurySerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PhysicalExamBodyPartInjury,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 19
class ProcedureViewsets(viewsets.ModelViewSet):
  serializer_class = ProcedureSerializer
  queryset = ProcedureSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Procedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Procedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = ProcedureSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     Procedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 20
class PrehospitalProcedureViewsets(viewsets.ModelViewSet):
  serializer_class = PrehospitalProcedureSerializer
  queryset = PrehospitalProcedureSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PrehospitalProcedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PrehospitalProcedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = PrehospitalProcedureSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     PrehospitalProcedure,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 21
class TransportationModeViewsets(viewsets.ModelViewSet):
  serializer_class = TransportationModeSerializer
  queryset = TransportationModeSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TransportationMode,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TransportationMode,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = TransportationModeSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     TransportationMode,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)

#! 22
class VitalSignViewsets(viewsets.ModelViewSet):
  serializer_class = VitalSignSerializer
  queryset = VitalSignSerializer.Meta.model.objects.all()
  # lookup_field = 'trauma_register_record_id'
  
  def partial_update(self, request, *args, **kwargs):
    kwargs['partial'] = True
    return super().partial_update(request, *args, **kwargs)
  
  # def update(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSign,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = self.get_serializer(
  #     data, 
  #     data=request.data, 
  #     partial=True
  #   )
  #   if serializer.is_valid(raise_exception=True):
  #     self.perform_update(serializer)
  #     return Response(serializer.data)
  #   return Response(serializer.errors)
  
  # def retrieve(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData,
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSign,
  #     trauma_register_record_id=patient_data,
  #   )
  #   serializer = VitalSignSerializer(data)
  #   return Response(serializer.data)
  
  # def destroy(self, request, trauma_register_record_id=None, *args, **kwargs):
  #   patient_data = get_object_or_404(
  #     PatientData, 
  #     trauma_register_record_id=trauma_register_record_id,
  #   )
  #   data = get_object_or_404(
  #     VitalSign,
  #     trauma_register_record_id=patient_data,
  #   )
  #   self.perform_destroy(data)
  #   return Response(status=status.HTTP_204_NO_CONTENT)