from datetime import datetime
from decimal import Decimal
from ...application.dtos import AuthTokensDTO, RegisterUserDTO, UserResponseDTO
from ...domain.entities import UserEntity
from ...domain.repositories import IPasswordHasher, ITokenService, IUserRepository


class RegisterUserUseCase:
    """
    Caso de uso: Registrar un nuevo usuario
    
    Responsabilidades:
    - Validar que el email no exista
    - Hashear la contraseña
    - Crear la entidad de usuario
    - Persistir en la base de datos
    - Generar tokens JWT
    
    Principio: Single Responsibility (SOLID)
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
    
    def execute(self, dto: RegisterUserDTO) -> AuthTokensDTO:
        """
        Ejecuta el caso de uso de registro
        
        Args:
            dto: Datos del usuario a registrar
            
        Returns:
            AuthTokensDTO con tokens y datos del usuario
            
        Raises:
            ValueError: Si el email ya existe o los datos son inválidos
        """
        # 1. Validar entrada
        dto.validate()
        
        # 2. Verificar que el email no exista
        if self._user_repository.email_exists(dto.email):
            raise ValueError("El email ya está registrado")
        
        # 3. Hashear la contraseña
        hashed_password = self._password_hasher.hash_password(dto.password)
        
        # 4. Crear entidad de usuario
        user_entity = UserEntity(
            id=None,
            name=dto.name,
            email=dto.email,
            password=hashed_password,
            phone=dto.phone,
            birthday=dto.birthday,
            money=Decimal('0.00'),
            icon=dto.icon,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            last_login=None,
            date_joined=datetime.now()
        )
        
        # 5. Persistir en la base de datos
        created_user = self._user_repository.create(user_entity)
        
        # 6. Generar tokens JWT
        tokens = self._token_service.generate_tokens(created_user)
        
        # 7. Retornar respuesta
        return AuthTokensDTO(
            access=tokens['access'],
            refresh=tokens['refresh'],
            user=UserResponseDTO.from_entity(created_user)
        )