from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    # Lista y creación
    path('', ProjectListView.as_view(), name='project-list'),
    
    # Detalle, actualización y eliminación
    path('<int:project_id>/', ProjectDetailView.as_view(), name='project-detail'),
]