"""
apps/authentication/domain/repositories.py

Interfaces de repositorios - Contratos del dominio
Define QUÉ operaciones se pueden hacer, no CÓMO
"""

from abc import ABC, abstractmethod
from typing import Optional
from .entities import UserEntity


class IUserRepository(ABC):
    """
    Interface del repositorio de usuarios
    
    Define el contrato que debe cumplir cualquier implementación
    de persistencia de usuarios (PostgreSQL, MongoDB, etc.)
    
    Principio: Dependency Inversion (SOLID)
    El dominio define la interface, la infraestructura la implementa
    """
    
    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        """
        Crea un nuevo usuario en la base de datos
        
        Args:
            user: Entidad de usuario a crear
            
        Returns:
            UserEntity con el ID asignado
            
        Raises:
            ValueError: Si el email ya existe
        """
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        """
        Busca un usuario por su ID
        
        Args:
            user_id: ID del usuario
            
        Returns:
            UserEntity si existe, None si no
        """
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[UserEntity]:
        """
        Busca un usuario por su email
        
        Args:
            email: Email del usuario
            
        Returns:
            UserEntity si existe, None si no
        """
        pass
    
    @abstractmethod
    def email_exists(self, email: str) -> bool:
        """
        Verifica si un email ya está registrado
        
        Args:
            email: Email a verificar
            
        Returns:
            True si existe, False si no
        """
        pass
    
    @abstractmethod
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
        pass
    
    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """
        Elimina un usuario (soft delete)
        
        Args:
            user_id: ID del usuario a eliminar
            
        Returns:
            True si se eliminó, False si no existe
        """
        pass
    
    @abstractmethod
    def list_all(self, limit: int = 100, offset: int = 0) -> list[UserEntity]:
        """
        Lista todos los usuarios activos
        
        Args:
            limit: Número máximo de resultados
            offset: Número de resultados a saltar
            
        Returns:
            Lista de UserEntity
        """
        pass


class IPasswordHasher(ABC):
    """
    Interface para el servicio de hashing de contraseñas
    
    Permite cambiar la implementación sin afectar el dominio
    """
    
    @abstractmethod
    def hash_password(self, plain_password: str) -> str:
        """
        Hashea una contraseña en texto plano
        
        Args:
            plain_password: Contraseña en texto plano
            
        Returns:
            Hash de la contraseña
        """
        pass
    
    @abstractmethod
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifica si una contraseña coincide con su hash
        
        Args:
            plain_password: Contraseña en texto plano
            hashed_password: Hash almacenado
            
        Returns:
            True si coincide, False si no
        """
        pass


class ITokenService(ABC):
    """
    Interface para el servicio de generación de tokens JWT
    """
    
    @abstractmethod
    def generate_tokens(self, user: UserEntity) -> dict:
        """
        Genera tokens de acceso y refresco para un usuario
        
        Args:
            user: Entidad de usuario
            
        Returns:
            Dict con 'access' y 'refresh' tokens
        """
        pass
    
    @abstractmethod
    def verify_token(self, token: str) -> bool:
        """
        Verifica si un token es válido
        
        Args:
            token: Token JWT a verificar
            
        Returns:
            True si es válido, False si no
        """
        pass
    
    @abstractmethod
    def refresh_access_token(self, refresh_token: str) -> str:
        """
        Genera un nuevo access token desde un refresh token
        
        Args:
            refresh_token: Refresh token válido
            
        Returns:
            Nuevo access token
            
        Raises:
            ValueError: Si el refresh token es inválido
        """
        pass
    
    @abstractmethod
    def blacklist_token(self, refresh_token: str) -> None:
        """
        Invalida un refresh token (logout)
        
        Args:
            refresh_token: Token a invalidar
        """
        pass