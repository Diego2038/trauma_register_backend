from rest_framework import serializers
from .models import *

class PatientDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = PatientData
    fields = '__all__'