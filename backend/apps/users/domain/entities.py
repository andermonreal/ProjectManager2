"""
apps/authentication/domain/entities.py

Entidades de dominio - Reglas de negocio puras
No dependen de Django, base de datos ni frameworks
"""

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
from decimal import Decimal


@dataclass
class UserEntity:
    """
    Entidad de Usuario - Representa el concepto de negocio
    
    Esta clase contiene solo la lógica de negocio del dominio,
    sin dependencias de frameworks o infraestructura.
    """
    id: Optional[int]
    name: str
    email: str
    password: str  # Hash de la contraseña
    phone: str
    birthday: date
    money: Decimal = Decimal('0.00')
    icon: Optional[str] = None
    is_active: bool = True
    is_staff: bool = False
    is_superuser: bool = False
    last_login: Optional[datetime] = None
    date_joined: Optional[datetime] = None
    
    def __post_init__(self):
        """Validaciones del dominio"""
        self._validate_email()
        self._validate_name()
        self._validate_phone()
        self._validate_birthday()
        self._validate_money()
    
    def _validate_email(self) -> None:
        """Valida que el email tenga formato correcto"""
        if not self.email or '@' not in self.email:
            raise ValueError("Email inválido")
        
        if len(self.email) > 150:
            raise ValueError("Email demasiado largo (máximo 150 caracteres)")
    
    def _validate_name(self) -> None:
        """Valida que el nombre sea válido"""
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("El nombre es obligatorio")
        
        if len(self.name) > 100:
            raise ValueError("Nombre demasiado largo (máximo 100 caracteres)")
    
    def _validate_phone(self) -> None:
        """Valida que el teléfono sea válido"""
        if not self.phone or len(self.phone.strip()) == 0:
            raise ValueError("El teléfono es obligatorio")
        
        if len(self.phone) > 20:
            raise ValueError("Teléfono demasiado largo (máximo 20 caracteres)")
    
    def _validate_birthday(self) -> None:
        """Valida que la fecha de nacimiento sea válida"""
        if not self.birthday:
            raise ValueError("La fecha de nacimiento es obligatoria")
        
        if self.birthday > date.today():
            raise ValueError("La fecha de nacimiento no puede ser futura")
        
        age = (date.today() - self.birthday).days // 365
        if age < 18:
            raise ValueError("Debes ser mayor de 18 años para registrarte")
    
    def _validate_money(self) -> None:
        """Valida que el saldo sea válido"""
        if self.money < 0:
            raise ValueError("El saldo no puede ser negativo")
    
    def is_adult(self) -> bool:
        """Verifica si el usuario es mayor de edad"""
        age = (date.today() - self.birthday).days // 365
        return age >= 18
    
    def can_make_purchase(self, amount: Decimal) -> bool:
        """Verifica si el usuario tiene saldo suficiente"""
        return self.money >= amount
    
    def deduct_money(self, amount: Decimal) -> None:
        """Deduce dinero del saldo del usuario"""
        if not self.can_make_purchase(amount):
            raise ValueError("Saldo insuficiente")
        self.money -= amount
    
    def add_money(self, amount: Decimal) -> None:
        """Añade dinero al saldo del usuario"""
        if amount <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.money += amount
    
    def deactivate(self) -> None:
        """Desactiva la cuenta del usuario"""
        self.is_active = False
    
    def activate(self) -> None:
        """Activa la cuenta del usuario"""
        self.is_active = True
    
    def update_last_login(self) -> None:
        """Actualiza la fecha del último login"""
        self.last_login = datetime.now()
    
    def to_dict(self) -> dict:
        """Convierte la entidad a diccionario (sin contraseña)"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'birthday': self.birthday.isoformat() if self.birthday else None,
            'money': float(self.money),
            'icon': self.icon,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'is_superuser': self.is_superuser,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'date_joined': self.date_joined.isoformat() if self.date_joined else None,
        }