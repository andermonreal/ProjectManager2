from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import ProjectEntity

class ProjectRepository(ABC):
    """
    Interfaz abstracta para el repositorio de proyectos
    Define el contrato que deben cumplir las implementaciones
    """
    
    @abstractmethod
    def find_by_user_id(self, user_id: int) -> List[ProjectEntity]:
        """Obtiene todos los proyectos de un usuario"""
        pass
    
    @abstractmethod
    def find_by_id(self, project_id: int) -> Optional[ProjectEntity]:
        """Obtiene un proyecto por su ID"""
        pass
    
    @abstractmethod
    def save(self, project: ProjectEntity) -> ProjectEntity:
        """Crea un nuevo proyecto"""
        pass
    
    @abstractmethod
    def update(self, project: ProjectEntity) -> ProjectEntity:
        """Actualiza un proyecto existente"""
        pass
    
    @abstractmethod
    def delete(self, project_id: int, user_id: int) -> bool:
        """Elimina un proyecto (verificando que pertenezca al usuario)"""
        pass