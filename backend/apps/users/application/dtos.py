"""
apps/users/application/dtos.py

Data Transfer Objects - Objetos para transferir datos entre capas
Separan la representación externa de la lógica interna
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional
from decimal import Decimal


@dataclass
class RegisterUserDTO:
    """
    DTO para el registro de usuarios
    Contiene solo los datos necesarios para registrar un usuario
    """
    name: str
    email: str
    password: str
    phone: str
    birthday: date
    icon: Optional[str] = None
    
    def validate(self) -> None:
        """Validaciones básicas de entrada"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("El nombre es obligatorio")
        
        if not self.email or '@' not in self.email:
            raise ValueError("Email inválido")
        
        if not self.password or len(self.password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        
        if not self.phone:
            raise ValueError("El teléfono es obligatorio")
        
        if not self.birthday:
            raise ValueError("La fecha de nacimiento es obligatoria")


@dataclass
class LoginUserDTO:
    """
    DTO para el login de usuarios
    """
    email: str
    password: str
    
    def validate(self) -> None:
        """Validaciones básicas de entrada"""
        if not self.email or '@' not in self.email:
            raise ValueError("Email inválido")
        
        if not self.password:
            raise ValueError("La contraseña es obligatoria")


@dataclass
class UserResponseDTO:
    """
    DTO para la respuesta de datos de usuario
    No incluye información sensible como la contraseña
    """
    id: int
    name: str
    email: str
    phone: str
    birthday: str
    money: float
    icon: Optional[str]
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: Optional[str]
    date_joined: Optional[str]
    
    @classmethod
    def from_entity(cls, entity):
        """Crea un DTO desde una entidad"""
        return cls(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            phone=entity.phone,
            birthday=entity.birthday.isoformat() if entity.birthday else None,
            money=float(entity.money),
            icon=entity.icon,
            is_active=entity.is_active,
            is_staff=entity.is_staff,
            is_superuser=entity.is_superuser,
            last_login=entity.last_login.isoformat() if entity.last_login else None,
            date_joined=entity.date_joined.isoformat() if entity.date_joined else None,
        )


@dataclass
class AuthTokensDTO:
    """
    DTO para los tokens de autenticación
    """
    access: str
    refresh: str
    user: UserResponseDTO


@dataclass
class LogoutDTO:
    """
    DTO para el logout
    """
    refresh_token: str
    
    def validate(self) -> None:
        """Validaciones básicas de entrada"""
        if not self.refresh_token:
            raise ValueError("El refresh token es obligatorio")
        
@dataclass
class UpdateUserDTO:
    """
    DTO para actualizar datos del usuario
    Solo permite modificar: nombre, teléfono, icono y contraseña
    """
    user_id: int
    name: Optional[str] = None
    phone: Optional[str] = None
    icon: Optional[str] = None
    current_password: Optional[str] = None  # Requerido si quiere cambiar password
    new_password: Optional[str] = None
    
    def validate(self) -> None:
        """Validaciones básicas de entrada"""
        # Al menos un campo debe estar presente
        if not any([self.name, self.phone, self.icon is not None, self.new_password]):
            raise ValueError("Debe proporcionar al menos un campo para actualizar")
        
        # Si quiere cambiar contraseña, debe proporcionar la actual
        if self.new_password:
            if not self.current_password:
                raise ValueError("Debe proporcionar la contraseña actual para cambiarla")
            
            if len(self.new_password) < 8:
                raise ValueError("La nueva contraseña debe tener al menos 8 caracteres")
        
        # Validar nombre si se proporciona
        if self.name is not None:
            if len(self.name.strip()) == 0:
                raise ValueError("El nombre no puede estar vacío")
            if len(self.name) > 100:
                raise ValueError("El nombre es demasiado largo (máximo 100 caracteres)")
        
        # Validar teléfono si se proporciona
        if self.phone is not None:
            if len(self.phone.strip()) == 0:
                raise ValueError("El teléfono no puede estar vacío")
            if len(self.phone) > 20:
                raise ValueError("El teléfono es demasiado largo (máximo 20 caracteres)")
        
        # Validar icono si se proporciona
        if self.icon is not None and len(self.icon) > 300:
            raise ValueError("La URL del icono es demasiado larga (máximo 300 caracteres)")