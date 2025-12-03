from ..dtos import LoginUserDTO, AuthTokensDTO, UserResponseDTO
from ...domain.repositories import IUserRepository, IPasswordHasher, ITokenService


class LoginUserUseCase:
    """
    Caso de uso: Iniciar sesión
    
    Responsabilidades:
    - Validar credenciales
    - Verificar que el usuario esté activo
    - Actualizar último login
    - Generar tokens JWT
    """
    
    def __init__(
        self,
        user_repository: IUserRepository,
        password_hasher: IPasswordHasher,
        token_service: ITokenService
    ):
        self._user_repository = user_repository
        self._password_hasher = password_hasher
        self._token_service = token_service
    
    def execute(self, dto: LoginUserDTO) -> AuthTokensDTO:
        """
        Ejecuta el caso de uso de login
        
        Args:
            dto: Credenciales del usuario
            
        Returns:
            AuthTokensDTO con tokens y datos del usuario
            
        Raises:
            ValueError: Si las credenciales son inválidas
        """
        # 1. Validar entrada
        dto.validate()
        
        # 2. Buscar usuario por email
        user = self._user_repository.find_by_email(dto.email)
        
        if user is None:
            raise ValueError("Credenciales inválidas")
        
        # 3. Verificar contraseña
        password_is_correct = self._password_hasher.verify_password(
            dto.password,
            user.password
        )
        
        if not password_is_correct:
            raise ValueError("Credenciales inválidas")
        
        # 4. Verificar que el usuario esté activo
        if not user.is_active:
            raise ValueError("Esta cuenta está inactiva")
        
        # 5. Actualizar último login
        user.update_last_login()
        self._user_repository.update(user)
        
        # 6. Generar tokens JWT
        tokens = self._token_service.generate_tokens(user)
        
        # 7. Retornar respuesta
        return AuthTokensDTO(
            access=tokens['access'],
            refresh=tokens['refresh'],
            user=UserResponseDTO.from_entity(user)
        )