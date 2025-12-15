"""
apps/users/presentation/serializers.py

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

class CreateSuperuserSerializer(serializers.Serializer):
    """Serializer para crear superusuario"""
    
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    phone = serializers.CharField(max_length=20, required=True)
    birthday = serializers.DateField(required=True)
    icon = serializers.CharField(max_length=300, required=False, allow_null=True, allow_blank=True)
    
    def validate_birthday(self, value):
        """Validar fecha de nacimiento"""
        if value > date.today():
            raise serializers.ValidationError("La fecha de nacimiento no puede ser futura")
        
        age = (date.today() - value).days // 365
        if age < 18:
            raise serializers.ValidationError("Debes ser mayor de 18 años")
        
        return value
    
    # def validate_password(self, value):
    #     """Validar complejidad de contraseña"""
    #     if len(value) < 12:
    #         raise serializers.ValidationError("La contraseña debe tener al menos 12 caracteres")
        
    #     if not any(c.isupper() for c in value):
    #         raise serializers.ValidationError("Debe contener al menos una mayúscula")
        
    #     if not any(c.islower() for c in value):
    #         raise serializers.ValidationError("Debe contener al menos una minúscula")
        
    #     if not any(c.isdigit() for c in value):
    #         raise serializers.ValidationError("Debe contener al menos un número")
        
    #     if not any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in value):
    #         raise serializers.ValidationError("Debe contener al menos un carácter especial")
        
    #     return value


class ListUsersSerializer(serializers.Serializer):
    """Serializer para parámetros de listado"""
    
    limit = serializers.IntegerField(default=50, min_value=1, max_value=100)
    offset = serializers.IntegerField(default=0, min_value=0)
    filter_by_active = serializers.BooleanField(required=False, allow_null=True)
    filter_by_staff = serializers.BooleanField(required=False, allow_null=True)
    search_email = serializers.CharField(required=False, allow_null=True, allow_blank=True)

class UserDetailSerializer(serializers.Serializer):
    """Serializer para respuesta detallada de usuario (admin)"""
    
    id = serializers.IntegerField()
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

class UpdateUserSerializer(serializers.Serializer):
    """
    Serializer para actualizar datos del usuario
    
    Todos los campos son opcionales, pero al menos uno debe estar presente
    """
    name = serializers.CharField(max_length=100, required=False, allow_blank=False)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=False)
    icon = serializers.CharField(max_length=300, required=False, allow_blank=True, allow_null=True)
    current_password = serializers.CharField(write_only=True, required=False)
    new_password = serializers.CharField(write_only=True, min_length=8, required=False)
    
    def validate(self, attrs):
        """Validaciones personalizadas"""
        # Si se proporciona new_password, current_password es obligatorio
        if 'new_password' in attrs and 'current_password' not in attrs:
            raise serializers.ValidationError({
                'current_password': 'Debe proporcionar la contraseña actual para cambiarla'
            })
        
        # Al menos un campo debe estar presente
        updatable_fields = ['name', 'phone', 'icon', 'new_password']
        if not any(field in attrs for field in updatable_fields):
            raise serializers.ValidationError(
                'Debe proporcionar al menos un campo para actualizar'
            )
        
        return attrs
    
    def validate_name(self, value):
        """Valida y normaliza el nombre"""
        if value:
            value = value.strip()
            if len(value) == 0:
                raise serializers.ValidationError("El nombre no puede estar vacío")
        return value
    
    def validate_phone(self, value):
        """Valida y normaliza el teléfono"""
        if value:
            value = value.strip()
            if len(value) == 0:
                raise serializers.ValidationError("El teléfono no puede estar vacío")
        return value