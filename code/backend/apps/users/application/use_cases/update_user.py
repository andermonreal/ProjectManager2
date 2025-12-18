"""

apps/authentication/application/use_cases/update_user.py

Caso de uso: Actualizar datos del usuario
"""

from ..dtos import UpdateUserDTO, UserResponseDTO
from ...domain.repositories import IUserRepository, IPasswordHasher


class UpdateUserUseCase:
    """
    Caso de uso: Actualizar información del usuario
    
    Responsabilidades:
    - Validar que el usuario exista
    - Verificar contraseña actual si se quiere cambiar
    - Actualizar solo los campos proporcionados
    - Hashear nueva contraseña si se proporciona
    - Persistir cambios
    
    Campos modificables:
    - name (nombre)
    - phone (teléfono)
    - icon (URL del icono/avatar)
    - password (contraseña, requiere verificación de la actual)
    """
    
    def __init__(
        self,
        user_repository: IUserRepository,
        password_hasher: IPasswordHasher
    ):
        self._user_repository = user_repository
        self._password_hasher = password_hasher
    
    def execute(self, dto: UpdateUserDTO) -> UserResponseDTO:
        """
        Ejecuta el caso de uso de actualización de usuario
        
        Args:
            dto: Datos del usuario a actualizar
            
        Returns:
            UserResponseDTO con los datos actualizados
            
        Raises:
            ValueError: Si el usuario no existe o la contraseña actual es incorrecta
        """
        # 1. Validar entrada
        dto.validate()
        
        # 2. Buscar usuario
        user = self._user_repository.find_by_id(dto.user_id)
        
        if user is None:
            raise ValueError("Usuario no encontrado")
        
        # 3. Si se quiere cambiar la contraseña, verificar la actual
        if dto.new_password:
            password_is_correct = self._password_hasher.verify_password(
                dto.current_password,
                user.password
            )
            
            if not password_is_correct:
                raise ValueError("La contraseña actual es incorrecta")
            
            # Hashear la nueva contraseña
            user.password = self._password_hasher.hash_password(dto.new_password)
        
        # 4. Actualizar campos proporcionados
        if dto.name is not None:
            user.name = dto.name.strip()
        
        if dto.phone is not None:
            user.phone = dto.phone.strip()
        
        if dto.icon is not None:
            user.icon = dto.icon if dto.icon.strip() else None
        
        # 5. Persistir cambios
        updated_user = self._user_repository.update(user)
        
        # 6. Retornar respuesta
        return UserResponseDTO.from_entity(updated_user)