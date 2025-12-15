from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class ProjectEntity:
    """
    Entidad de dominio para Proyecto
    Representa un proyecto en el sistema
    """
    id: Optional[int]
    user_id: int
    title: str
    description: Optional[str]
    content: Optional[str]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def validate(self):
        """Valida las reglas de negocio del proyecto"""
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("El título del proyecto es obligatorio")
        
        if len(self.title) > 200:
            raise ValueError("El título no puede exceder 200 caracteres")
        
        if self.user_id is None or self.user_id <= 0:
            raise ValueError("El proyecto debe pertenecer a un usuario válido")
    
    @staticmethod
    def create(
        user_id: int,
        title: str,
        description: str = None,
        content: str = None
    ) -> 'ProjectEntity':
        """Factory method para crear un nuevo proyecto"""
        project = ProjectEntity(
            id=None,
            user_id=user_id,
            title=title.strip(),
            description=description,
            content=content
        )
        project.validate()
        return project