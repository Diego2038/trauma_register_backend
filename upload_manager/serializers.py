from rest_framework import serializers

class UploadSerializer(serializers.Serializer):
  
  class Meta:
    fields = ["file", "user"]