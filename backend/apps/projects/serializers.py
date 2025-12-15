from rest_framework import serializers

class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(max_length=1000, required=False, allow_null=True, allow_blank=True)
    content = serializers.CharField(required=False, allow_null=True, allow_blank=True)