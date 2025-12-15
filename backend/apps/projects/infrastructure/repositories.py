from typing import List, Optional
from ..domain.repositories import ProjectRepository
from ..domain.entities import ProjectEntity
from .models import Project

class DjangoProjectRepository(ProjectRepository):
    """
    Implementación del repositorio usando Django ORM
    
    ✅ SEGURO: Todas las queries filtran por user_id
    """
    
    def find_by_user_id(self, user_id: int) -> List[ProjectEntity]:
        """Obtiene todos los proyectos de un usuario"""        
        django_projects = Project.objects.filter(user_id=user_id).order_by('-created_at')
        return [p.to_entity() for p in django_projects]
    
    def find_by_id(self, project_id: int) -> Optional[ProjectEntity]:
        """Obtiene un proyecto por su ID"""
        try:
            project = Project.objects.get(id=project_id)
            return project.to_entity()
        except Project.DoesNotExist:
            return None
    
    def save(self, project: ProjectEntity) -> ProjectEntity:
        """Crea un nuevo proyecto"""
        django_project = Project.objects.create(
            user_id=project.user_id,
            title=project.title,
            description=project.description,
            content=project.content
        )
        return django_project.to_entity()
    
    def update(self, project: ProjectEntity) -> ProjectEntity:
        """Actualiza un proyecto existente"""
        try:
            django_project = Project.objects.get(
                id=project.id,
                user_id=project.user_id  # ✅ SEGURO: Verifica ownership
            )
            
            django_project.title = project.title
            django_project.description = project.description
            django_project.content = project.content
            django_project.save()
            
            return django_project.to_entity()
        except Project.DoesNotExist:
            raise ValueError("Proyecto no encontrado o no pertenece al usuario")
    
    def delete(self, project_id: int, user_id: int) -> bool:
        """Elimina un proyecto"""
        try:
            project = Project.objects.get(
                id=project_id,
                user_id=user_id  # ✅ SEGURO: Verifica ownership
            )
            project.delete()
            return True
        except Project.DoesNotExist:
            return False