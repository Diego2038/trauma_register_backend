from rest_framework import serializers

class UploadSerializer(serializers.Serializer):
  
  class Meta:
    fields = ["file", "user", "update_data", "only_update",]