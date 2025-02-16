from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import PatientDataSerializer
from .models import PatientData

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
