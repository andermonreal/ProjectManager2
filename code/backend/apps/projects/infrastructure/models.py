from django.db import models
from apps.users.infrastructure.models import User

class Project(models.Model):
    """
    Modelo de Django para proyectos
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'projects'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.user.email}"
    
    def to_entity(self):
        """Convierte el modelo Django a entidad de dominio"""
        print("Converting Project model to ProjectEntity")
        from ..domain.entities import ProjectEntity
        print(f"Converting Project(id={self.id}) to ProjectEntity")
        return ProjectEntity(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            description=self.description,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at
        )