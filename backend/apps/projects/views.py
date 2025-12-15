from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Obtener TODOS los proyectos del usuario autenticado
        """
        user = request.user

        projects = Project.objects.filter(user=user).order_by("-created_at")
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Crear un nuevo proyecto para el usuario autenticado
        """
        serializer = ProjectSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        project = serializer.save(user=request.user)

        return Response(
            ProjectSerializer(project).data,
            status=status.HTTP_201_CREATED
        )
