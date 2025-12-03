from ...domain.repositories import ITokenService


class RefreshTokenUseCase:
    """
    Caso de uso: Refrescar access token
    
    Responsabilidades:
    - Validar refresh token
    - Generar nuevo access token
    """
    
    def __init__(self, token_service: ITokenService):
        self._token_service = token_service
    
    def execute(self, refresh_token: str) -> dict:
        """
        Ejecuta el caso de uso de refresh token
        
        Args:
            refresh_token: Refresh token válido
            
        Returns:
            Dict con nuevo access token
            
        Raises:
            ValueError: Si el token es inválido
        """
        if not refresh_token:
            raise ValueError("Refresh token es obligatorio")
        
        # Generar nuevo access token
        new_access_token = self._token_service.refresh_access_token(refresh_token)
        
        return {
            'access': new_access_token
        }