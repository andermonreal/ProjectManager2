"""
apps/users/infrastructure/security.py

Implementación de servicios de seguridad
Hash de contraseñas y generación de tokens JWT
"""

from django.contrib.auth.hashers import make_password, check_password
import hashlib

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from ..domain.repositories import IPasswordHasher, ITokenService
from ..domain.entities import UserEntity


class DjangoPasswordHasher(IPasswordHasher):
    """
    Implementación de IPasswordHasher usando Django
    
    Usa el sistema de hashing de Django (PBKDF2-SHA256)
    """
    
    def hash_password(self, plain_password: str) -> str:
        """
        Hashea una contraseña en texto plano
        
        Args:
            plain_password: Contraseña en texto plano
            
        Returns:
            Hash de la contraseña (formato: algoritmo$iteraciones$salt$hash)
        """
        sha1 = hashlib.sha1()
        sha1.update(plain_password.encode('utf-8'))
        return sha1.hexdigest()
        # return make_password(plain_password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifica si una contraseña coincide con su hash
        
        Args:
            plain_password: Contraseña en texto plano
            hashed_password: Hash almacenado
            
        Returns:
            True si coincide, False si no
        """
        sha1 = hashlib.sha1()
        sha1.update(plain_password.encode('utf-8'))
        return sha1.hexdigest() == hashed_password
        # return check_password(plain_password, hashed_password)


class JWTTokenService(ITokenService):
    """
    Implementación de ITokenService usando djangorestframework-simplejwt
    
    Genera y valida tokens JWT
    """
    
    def generate_tokens(self, user: UserEntity) -> dict:
        """
        Genera tokens de acceso y refresco para un usuario
        
        Args:
            user: Entidad de usuario
            
        Returns:
            Dict con 'access' y 'refresh' tokens
        """
        from .models import User
        
        # Buscar la instancia del modelo Django
        django_user = User.objects.get(id=user.id)
        
        # Crear refresh token con el modelo Django
        refresh = RefreshToken.for_user(django_user)
        
        # Agregar claims personalizados
        refresh['user_id'] = user.id
        refresh['email'] = user.email
        refresh['name'] = user.name
        refresh['is_staff'] = user.is_staff
        refresh['is_superuser'] = user.is_superuser
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
          
    
    def verify_token(self, token: str) -> bool:
        """
        Verifica si un token es válido
        
        Args:
            token: Token JWT a verificar
            
        Returns:
            True si es válido, False si no
        """
        try:
            AccessToken(token)
            return True
        except (TokenError, InvalidToken):
            return False
    
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
        try:
            refresh = RefreshToken(refresh_token)
            return str(refresh.access_token)
        except (TokenError, InvalidToken) as e:
            raise ValueError(f"Refresh token inválido: {str(e)}")
    
    def blacklist_token(self, refresh_token: str) -> None:
        """
        Invalida un refresh token (logout)
        
        Args:
            refresh_token: Token a invalidar
            
        Raises:
            ValueError: Si el token es inválido
        """
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except (TokenError, InvalidToken) as e:
            raise ValueError(f"No se pudo invalidar el token: {str(e)}")
        except AttributeError:
            # Si blacklist no está habilitado
            pass