from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class CreateProjectDTO:
    """DTO para crear un nuevo proyecto"""
    title: str
    description: Optional[str] = None
    content: Optional[str] = None
    
    def validate(self):
        """Valida el DTO"""
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("El título es obligatorio")
        
        if len(self.title) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")

@dataclass
class ProjectResponseDTO:
    """DTO para respuestas de proyectos"""
    id: int
    user_id: int
    title: str
    description: Optional[str]
    content: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
    @staticmethod
    def from_entity(entity) -> 'ProjectResponseDTO':
        """Convierte una entidad a DTO"""
        return ProjectResponseDTO(
            id=entity.id,
            user_id=entity.user_id,
            title=entity.title,
            description=entity.description,
            content=entity.content,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

@dataclass
class UpdateProjectDTO:
    """DTO para actualizar un proyecto"""
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    
    def validate(self):
        """Valida el DTO"""
        if self.title is not None:
            if len(self.title.strip()) == 0:
                raise ValueError("El título no puede estar vacío")
            if len(self.title) > 200:
                raise ValueError("El título no puede exceder 200 caracteres")