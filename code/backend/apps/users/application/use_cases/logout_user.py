from ...application.dtos import LogoutDTO
from ...domain.repositories import ITokenService


class LogoutUserUseCase:
    """
    Caso de uso: Cerrar sesión
    
    Responsabilidades:
    - Invalidar el refresh token (blacklist)
    """
    
    def __init__(self, token_service: ITokenService):
        self._token_service = token_service
    
    def execute(self, dto: LogoutDTO) -> None:
        """
        Ejecuta el caso de uso de logout
        
        Args:
            dto: Datos del logout (refresh token)
            
        Raises:
            ValueError: Si el token es inválido
        """
        # 1. Validar entrada
        dto.validate()
        
        # 2. Invalidar refresh token
        self._token_service.blacklist_token(dto.refresh_token)