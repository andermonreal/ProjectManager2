from typing import List
from ...domain.repositories import ProjectRepository
from ...application.dtos import ProjectResponseDTO

class GetUserProjectsUseCase:
    """
    Caso de uso: Obtener todos los proyectos de un usuario
    
    ✅ SEGURO: Solo obtiene proyectos del usuario autenticado
    """
    
    def __init__(self, project_repository: ProjectRepository):
        self._repository = project_repository
    
    def execute(self, user_id: int) -> List[ProjectResponseDTO]:
        """
        Obtiene todos los proyectos del usuario especificado
        
        Args:
            user_id: ID del usuario autenticado (extraído del JWT)
        
        Returns:
            Lista de proyectos en formato DTO
        """
        # Obtener proyectos del repositorio
        projects = self._repository.find_by_user_id(user_id)
        
        # Convertir entidades a DTOs
        return [ProjectResponseDTO.from_entity(p) for p in projects]