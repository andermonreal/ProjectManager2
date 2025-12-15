from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..application.use_cases.get_user_projects import GetUserProjectsUseCase
from ..application.use_cases.create_project import CreateProjectUseCase
from ..infrastructure.repositories import DjangoProjectRepository
from .serializers import (
    CreateProjectSerializer,
    ProjectResponseSerializer,
    UpdateProjectSerializer
)
from ..application.dtos import CreateProjectDTO

class ProjectListView(APIView):
    """
    Vista para listar y crear proyectos
    
    ✅ SEGURO: Requiere autenticación JWT
    ✅ SEGURO: El user_id se extrae del token, no del request
    """
    permission_classes = [IsAuthenticated]  # ✅ CRÍTICO: Requiere JWT válido
    
    def get(self, request):
        """
        GET /api/projects/
        
        Obtiene todos los proyectos del usuario autenticado
        
        Headers:
            Authorization: Bearer <jwt_token>
        
        Returns:
            200: Lista de proyectos
            401: No autenticado
        """
        # ✅ SEGURO: El user_id viene del JWT decodificado por DRF
        user_id = request.user.id
        
        # Inyectar dependencias
        repository = DjangoProjectRepository()
        use_case = GetUserProjectsUseCase(repository)
        
        try:
            # Ejecutar caso de uso
            projects = use_case.execute(user_id)
            
            # Serializar respuesta
            serializer = ProjectResponseSerializer(projects, many=True)
            print(serializer.data)
            print(len(projects))
            return Response({
                'message': 'Proyectos obtenidos exitosamente',
                'data': serializer.data,
                'count': len(projects)
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'error': 'Error al obtener proyectos',
                'detail': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        """
        POST /api/projects/
        
        Crea un nuevo proyecto para el usuario autenticado
        
        Headers:
            Authorization: Bearer <jwt_token>
        
        Body:
            {
                "title": "Mi Proyecto",
                "description": "Descripción opcional",
                "content": "Contenido opcional"
            }
        
        Returns:
            201: Proyecto creado
            400: Datos inválidos
            401: No autenticado
        """
        # ✅ SEGURO: El user_id viene del JWT
        user_id = request.user.id
        
        # 1. Validar entrada
        serializer = CreateProjectSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Crear DTO
        dto = CreateProjectDTO(
            title=serializer.validated_data['title'],
            description=serializer.validated_data.get('description'),
            content=serializer.validated_data.get('content')
        )
        
        # 3. Inyectar dependencias
        repository = DjangoProjectRepository()
        use_case = CreateProjectUseCase(repository)
        
        try:
            # 4. Ejecutar caso de uso
            # ✅ SEGURO: Pasamos el user_id del JWT, no del body
            project = use_case.execute(dto, user_id=user_id)
            
            # 5. Serializar respuesta
            response_serializer = ProjectResponseSerializer(project)
            
            return Response({
                'message': 'Proyecto creado exitosamente',
                'data': response_serializer.data
            }, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': 'Error al crear proyecto',
                'detail': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProjectDetailView(APIView):
    """
    Vista para obtener, actualizar y eliminar un proyecto específico
    
    ✅ SEGURO: Verifica que el proyecto pertenezca al usuario autenticado
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, project_id):
        """
        GET /api/projects/<id>/
        
        Obtiene un proyecto específico
        
        Returns:
            200: Proyecto encontrado
            404: Proyecto no encontrado o no pertenece al usuario
        """
        user_id = request.user.id
        repository = DjangoProjectRepository()
        
        try:
            project = repository.find_by_id(project_id)
            
            if not project:
                return Response({
                    'error': 'Proyecto no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # ✅ SEGURO: Verificar ownership
            if project.user_id != user_id:
                return Response({
                    'error': 'No tienes permiso para acceder a este proyecto'
                }, status=status.HTTP_403_FORBIDDEN)
            
            serializer = ProjectResponseSerializer(project)
            
            return Response({
                'message': 'Proyecto obtenido exitosamente',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, project_id):
        """
        PUT /api/projects/<id>/
        
        Actualiza un proyecto completo
        """
        user_id = request.user.id
        repository = DjangoProjectRepository()
        
        try:
            # 1. Verificar que existe y pertenece al usuario
            project = repository.find_by_id(project_id)
            
            if not project or project.user_id != user_id:
                return Response({
                    'error': 'Proyecto no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
            
            # 2. Validar datos
            serializer = UpdateProjectSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # 3. Actualizar entidad
            if 'title' in serializer.validated_data:
                project.title = serializer.validated_data['title']
            if 'description' in serializer.validated_data:
                project.description = serializer.validated_data['description']
            if 'content' in serializer.validated_data:
                project.content = serializer.validated_data['content']
            
            project.validate()
            
            # 4. Guardar cambios
            updated_project = repository.update(project)
            
            response_serializer = ProjectResponseSerializer(updated_project)
            
            return Response({
                'message': 'Proyecto actualizado exitosamente',
                'data': response_serializer.data
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, project_id):
        """
        DELETE /api/projects/<id>/
        
        Elimina un proyecto
        """
        user_id = request.user.id
        repository = DjangoProjectRepository()
        
        try:
            # ✅ SEGURO: El repositorio verifica ownership
            deleted = repository.delete(project_id, user_id)
            
            if not deleted:
                return Response({
                    'error': 'Proyecto no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
            
            return Response({
                'message': 'Proyecto eliminado exitosamente'
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)