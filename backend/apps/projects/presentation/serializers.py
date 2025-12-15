from rest_framework import serializers

class CreateProjectSerializer(serializers.Serializer):
    """
    Serializer para crear un proyecto
    
    ✅ SEGURO: NO incluye user_id (se toma del JWT)
    """
    title = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(required=False, allow_blank=True)
    content = serializers.CharField(required=False, allow_blank=True)

class ProjectResponseSerializer(serializers.Serializer):
    """Serializer para respuestas de proyectos"""
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    content = serializers.CharField(allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

class UpdateProjectSerializer(serializers.Serializer):
    """Serializer para actualizar un proyecto"""
    title = serializers.CharField(max_length=200, required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    content = serializers.CharField(required=False, allow_blank=True)