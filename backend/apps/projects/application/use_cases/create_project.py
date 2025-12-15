from ...domain.repositories import ProjectRepository
from ...domain.entities import ProjectEntity
from ...application.dtos import CreateProjectDTO, ProjectResponseDTO

class CreateProjectUseCase:
    """
    Caso de uso: Crear un nuevo proyecto
    
    ✅ SEGURO: El user_id se toma del JWT, no del request body
    """
    
    def __init__(self, project_repository: ProjectRepository):
        self._repository = project_repository
    
    def execute(self, dto: CreateProjectDTO, user_id: int) -> ProjectResponseDTO:
        """
        Crea un nuevo proyecto para el usuario autenticado
        
        Args:
            dto: Datos del proyecto a crear
            user_id: ID del usuario autenticado (extraído del JWT)
        
        Returns:
            Proyecto creado en formato DTO
        """
        # 1. Validar DTO
        dto.validate()
        
        # 2. Crear entidad de dominio
        project = ProjectEntity.create(
            user_id=user_id,  # ✅ SEGURO: Viene del JWT
            title=dto.title,
            description=dto.description,
            content=dto.content
        )
        
        # 3. Guardar en el repositorio
        saved_project = self._repository.save(project)
        
        # 4. Retornar DTO de respuesta
        return ProjectResponseDTO.from_entity(saved_project)