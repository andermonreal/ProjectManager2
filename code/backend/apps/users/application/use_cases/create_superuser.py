from decimal import Decimal
from ..dtos import CreateSuperuserDTO, UserResponseDTO, AuthTokensDTO
from ...domain.entities import UserEntity

class CreateSuperuserUseCase:
    """
    Caso de uso: Crear un superusuario
    
    Responsabilidades:
    - Validar que el email no exista
    - Validar requisitos de contraseña segura
    - Crear usuario con privilegios de superusuario
    - Hashear contraseña
    - Establecer permisos de admin
    
    Reglas de negocio:
    - Solo puede haber un número limitado de superusuarios
    - La contraseña debe ser muy segura
    - Se registra en logs de auditoría
    """
    
    MAX_SUPERUSERS = 5  # Límite de superusuarios
    
    def __init__(
        self,
        user_repository,
        password_hasher,
        token_service
    ):
        self._user_repository = user_repository
        self._password_hasher = password_hasher
        self._token_service = token_service
    
    def execute(self, dto: CreateSuperuserDTO) -> CreateSuperuserDTO:
        """
        Ejecuta el caso de uso de creación de superusuario
        
        Args:
            dto: Datos del superusuario a crear
            
        Returns:
            UserResponseDTO con los datos del superusuario creado
            
        Raises:
            ValueError: Si el email existe, hay demasiados superusuarios,
                       o las validaciones fallan
        """
        # 1. Validar entrada
        dto.validate()
        
        # 2. Verificar que el email no exista
        if self._user_repository.email_exists(dto.email):
            raise ValueError("El email ya está registrado")
        
        # 3. Verificar límite de superusuarios
        superuser_count = self._count_superusers()
        if superuser_count >= self.MAX_SUPERUSERS:
            raise ValueError(
                f"No se pueden crear más de {self.MAX_SUPERUSERS} superusuarios. "
                f"Actualmente hay {superuser_count}."
            )
        
        # 4. Hashear la contraseña
        hashed_password = self._password_hasher.hash_password(dto.password)
        
        # 5. Crear entidad de superusuario
        from datetime import datetime
        
        superuser_entity = UserEntity(
            id=None,
            name=dto.name,
            email=dto.email,
            password=hashed_password,
            phone=dto.phone,
            birthday=dto.birthday,
            money=Decimal('0.00'),
            icon=dto.icon,
            is_active=True,
            is_staff=True,        # ✅ Es staff
            is_superuser=True,    # ✅ Es superusuario
            last_login=None,
            date_joined=datetime.now()
        )
        
        # 6. Persistir en la base de datos
        created_superuser = self._user_repository.create(superuser_entity)
        
        # 7. Log de auditoría (opcional)
        self._log_superuser_creation(created_superuser)
        
        # 8. Retornar respuesta
        tokens = self._token_service.generate_tokens(created_superuser)
        
        # 7. Retornar respuesta
        return AuthTokensDTO(
            access=tokens['access'],
            refresh=tokens['refresh'],
            user=UserResponseDTO.from_entity(created_superuser)
        )
    
    def _count_superusers(self) -> int:
        """Cuenta cuántos superusuarios hay actualmente"""
        # Implementación simplificada
        # En producción, esto debería ser un método del repositorio
        from ...infrastructure.models import User
        return User.objects.filter(is_superuser=True, is_active=True).count()
    
    def _log_superuser_creation(self, superuser: UserEntity) -> None:
        """Registra la creación de un superusuario en logs de auditoría"""
        import logging
        logger = logging.getLogger('security.audit')
        logger.warning(
            f"SUPERUSER CREATED: {superuser.email} (ID: {superuser.id}) "
            f"at {superuser.date_joined}"
        )