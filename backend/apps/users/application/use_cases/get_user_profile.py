from ...application.dtos import UserResponseDTO
from ...domain.repositories import IUserRepository


class GetUserProfileUseCase:
    """
    Caso de uso: Obtener perfil de usuario
    
    Responsabilidades:
    - Buscar usuario por ID
    - Retornar datos del usuario
    """
    
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository
    
    def execute(self, user_id: int) -> UserResponseDTO:
        """
        Ejecuta el caso de uso de obtener perfil
        
        Args:
            user_id: ID del usuario
            
        Returns:
            UserResponseDTO con los datos del usuario
            
        Raises:
            ValueError: Si el usuario no existe
        """
        # 1. Buscar usuario
        user = self._user_repository.find_by_id(user_id)
        
        if user is None:
            raise ValueError("Usuario no encontrado")
        
        # 2. Retornar respuesta
        return UserResponseDTO.from_entity(user)
