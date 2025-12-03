"""
apps/users/infrastructure/repositories.py

Implementación de los repositorios - Capa de infraestructura
Implementa las interfaces definidas en el dominio
"""

from typing import Optional
from django.db import transaction

from ..domain.repositories import IUserRepository
from ..domain.entities import UserEntity
from .models import User


class DjangoUserRepository(IUserRepository):
    """
    Implementación del repositorio de usuarios usando Django ORM
    
    Implementa IUserRepository definido en el dominio
    Principio: Dependency Inversion (SOLID)
    """
    
    @transaction.atomic
    def create(self, user: UserEntity) -> UserEntity:
        """
        Crea un nuevo usuario en PostgreSQL
        
        Args:
            user: Entidad de usuario a crear
            
        Returns:
            UserEntity con el ID asignado por la BD
            
        Raises:
            ValueError: Si el email ya existe
        """
        # Verificar que no exista
        if self.email_exists(user.email):
            raise ValueError(f"El email {user.email} ya está registrado")
        
        # Convertir entidad a modelo Django
        django_user = User(
            name=user.name,
            email=user.email,
            password=user.password,  # Ya debe venir hasheado
            phone=user.phone,
            birthday=user.birthday,
            money=user.money,
            icon=user.icon,
            is_active=user.is_active,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            date_joined=user.date_joined
        )
        
        # Guardar en la BD
        django_user.save()
        
        # Retornar entidad con el ID asignado
        return django_user.to_entity()
    
    def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        """
        Busca un usuario por su ID
        
        Args:
            user_id: ID del usuario
            
        Returns:
            UserEntity si existe, None si no
        """
        try:
            django_user = User.objects.get(id=user_id)
            return django_user.to_entity()
        except User.DoesNotExist:
            return None
    
    def find_by_email(self, email: str) -> Optional[UserEntity]:
        """
        Busca un usuario por su email
        
        Args:
            email: Email del usuario
            
        Returns:
            UserEntity si existe, None si no
        """
        try:
            django_user = User.objects.get(email=email)
            return django_user.to_entity()
        except User.DoesNotExist:
            return None
    
    def email_exists(self, email: str) -> bool:
        """
        Verifica si un email ya está registrado
        
        Args:
            email: Email a verificar
            
        Returns:
            True si existe, False si no
        """
        return User.objects.filter(email=email).exists()
    
    @transaction.atomic
    def update(self, user: UserEntity) -> UserEntity:
        """
        Actualiza un usuario existente
        
        Args:
            user: Entidad de usuario con los datos actualizados
            
        Returns:
            UserEntity actualizado
            
        Raises:
            ValueError: Si el usuario no existe
        """
        try:
            django_user = User.objects.get(id=user.id)
            
            # Actualizar campos
            django_user.name = user.name
            django_user.email = user.email
            django_user.phone = user.phone
            django_user.birthday = user.birthday
            django_user.money = user.money
            django_user.icon = user.icon
            django_user.is_active = user.is_active
            django_user.is_staff = user.is_staff
            django_user.is_superuser = user.is_superuser
            django_user.last_login = user.last_login
            
            # NO actualizar password aquí (se hace con set_password)
            if user.password and user.password != django_user.password:
                django_user.password = user.password
            
            django_user.save()
            
            return django_user.to_entity()
            
        except User.DoesNotExist:
            raise ValueError(f"Usuario con ID {user.id} no existe")
    
    @transaction.atomic
    def delete(self, user_id: int) -> bool:
        """
        Elimina un usuario (soft delete - marca como inactivo)
        
        Args:
            user_id: ID del usuario a eliminar
            
        Returns:
            True si se eliminó, False si no existe
        """
        try:
            django_user = User.objects.get(id=user_id)
            django_user.is_active = False
            django_user.save()
            return True
        except User.DoesNotExist:
            return False
    
    def list_all(self, limit: int = 100, offset: int = 0) -> list[UserEntity]:
        """
        Lista todos los usuarios activos
        
        Args:
            limit: Número máximo de resultados
            offset: Número de resultados a saltar
            
        Returns:
            Lista de UserEntity
        """
        django_users = User.objects.filter(
            is_active=True
        ).order_by('-date_joined')[offset:offset + limit]
        
        return [user.to_entity() for user in django_users]