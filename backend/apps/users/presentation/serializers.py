"""
apps/authentication/presentation/serializers.py

Serializers - Capa de presentación
Validan y transforman datos HTTP a DTOs
"""

from rest_framework import serializers
from datetime import date


class RegisterUserSerializer(serializers.Serializer):
    """Serializer para el registro de usuarios"""
    
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    phone = serializers.CharField(max_length=20, required=True)
    birthday = serializers.DateField(required=True)
    icon = serializers.CharField(max_length=300, required=False, allow_null=True, allow_blank=True)
    
    def validate_birthday(self, value):
        """Valida que la fecha de nacimiento sea válida"""
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser futura")
        
        age = (date.today() - value).days // 365
        if age < 18:
            raise serializers.ValidationError("Debes ser mayor de 18 años")
        
        return value
    
    def validate_email(self, value):
        """Normaliza el email"""
        return value.lower().strip()


class LoginUserSerializer(serializers.Serializer):
    """Serializer para el login de usuarios"""
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    
    def validate_email(self, value):
        """Normaliza el email"""
        return value.lower().strip()


class LogoutSerializer(serializers.Serializer):
    """Serializer para el logout"""
    
    refresh_token = serializers.CharField(required=True)


class UserResponseSerializer(serializers.Serializer):
    """Serializer para la respuesta de datos de usuario"""
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    birthday = serializers.DateField()
    money = serializers.DecimalField(max_digits=10, decimal_places=2)
    icon = serializers.CharField(allow_null=True)
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    last_login = serializers.DateTimeField(allow_null=True)
    date_joined = serializers.DateTimeField()


class AuthTokensSerializer(serializers.Serializer):
    """Serializer para los tokens de autenticación"""
    
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = UserResponseSerializer()