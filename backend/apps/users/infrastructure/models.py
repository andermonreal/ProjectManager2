"""
apps/users/infrastructure/models.py

Modelos de Django - Capa de infraestructura/persistencia
Mapean las entidades de dominio a tablas de PostgreSQL
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manager personalizado para el modelo User"""
    
    def create_user(self, email, name, password=None, **extra_fields):
        """Crea y guarda un usuario normal"""
        if not email:
            raise ValueError('El email es obligatorio')
        if not name:
            raise ValueError('El nombre es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        """Crea y guarda un superusuario"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # Valores por defecto para campos obligatorios
        extra_fields.setdefault('phone', '000000000')
        extra_fields.setdefault('birthday', '2000-01-01')
        
        return self.create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de Usuario personalizado para Django
    
    Mapea la tabla 'users' de PostgreSQL
    Sigue tu esquema SQL exacto
    """
    
    # Campos básicos
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, unique=True, null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    
    # Campos monetarios e icono
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    icon = models.CharField(max_length=300, null=True, blank=True)
    
    # Permisos y estado
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # Timestamps
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Configuración del manager
    objects = CustomUserManager()
    
    # Campo para autenticación
    USERNAME_FIELD = 'email'  # Usar email para login
    REQUIRED_FIELDS = ['name']  # Campos requeridos además de email y password
    
    class Meta:
        db_table = 'users'  # Nombre de la tabla en PostgreSQL
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        app_label = "users"
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def get_full_name(self):
        """Retorna el nombre completo del usuario"""
        return self.name
    
    def get_short_name(self):
        """Retorna el nombre corto del usuario"""
        return self.name
    
    def to_entity(self):
        """
        Convierte el modelo de Django a entidad de dominio
        
        Este método es el puente entre infraestructura y dominio
        """
        from ..domain.entities import UserEntity
        
        return UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password,
            phone=self.phone,
            birthday=self.birthday,
            money=self.money,
            icon=self.icon,
            is_active=self.is_active,
            is_staff=self.is_staff,
            is_superuser=self.is_superuser,
            last_login=self.last_login,
            date_joined=self.date_joined
        )
    
    @classmethod
    def from_entity(cls, entity):
        """
        Crea un modelo de Django desde una entidad de dominio
        
        Este método es el puente entre dominio e infraestructura
        """
        return cls(
            id=entity.id,
            name=entity.name,
            email=entity.email,
            password=entity.password,
            phone=entity.phone,
            birthday=entity.birthday,
            money=entity.money,
            icon=entity.icon,
            is_active=entity.is_active,
            is_staff=entity.is_staff,
            is_superuser=entity.is_superuser,
            last_login=entity.last_login,
            date_joined=entity.date_joined
        )