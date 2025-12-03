"""
apps/authentication/presentation/views.py

Views - Capa de presentación
Maneja peticiones HTTP y delega a los casos de uso
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    RegisterUserSerializer,
    LoginUserSerializer,
    LogoutSerializer,
    AuthTokensSerializer,
    UserResponseSerializer
)
from ..application.dtos import RegisterUserDTO, LoginUserDTO, LogoutDTO
from ..application.use_cases.register_user import RegisterUserUseCase
from ..application.use_cases.login_user import LoginUserUseCase
from ..application.use_cases.logout_user import LogoutUserUseCase
from ..application.use_cases.get_user_profile import GetUserProfileUseCase
from ..infrastructure.repositories import DjangoUserRepository
from ..infrastructure.security import DjangoPasswordHasher, JWTTokenService


class RegisterView(APIView):
    """
    Vista para registrar nuevos usuarios
    
    POST /api/auth/register/
    """
    permission_classes = (AllowAny,)
    
    def post(self, request):
        # 1. Validar entrada con serializer
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 2. Crear DTO
        dto = RegisterUserDTO(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            phone=serializer.validated_data['phone'],
            birthday=serializer.validated_data['birthday'],
            icon=serializer.validated_data.get('icon')
        )
        
        # 3. Inyectar dependencias
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        # 4. Ejecutar caso de uso
        use_case = RegisterUserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            result = use_case.execute(dto)
            
            # 5. Serializar respuesta
            response_serializer = AuthTokensSerializer(result)
            
            return Response(
                {
                    'message': 'Usuario registrado exitosamente',
                    'data': response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):
    """
    Vista para iniciar sesión
    
    POST /api/auth/login/
    """
    permission_classes = (AllowAny,)
    
    def post(self, request):
        # 1. Validar entrada
        serializer = LoginUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 2. Crear DTO
        dto = LoginUserDTO(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        
        # 3. Inyectar dependencias
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        # 4. Ejecutar caso de uso
        use_case = LoginUserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            result = use_case.execute(dto)
            
            # 5. Serializar respuesta
            response_serializer = AuthTokensSerializer(result)
            
            return Response(
                {
                    'message': 'Login exitoso',
                    'data': response_serializer.data
                },
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):
    """
    Vista para cerrar sesión
    
    POST /api/auth/logout/
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    
    def post(self, request):
        # 1. Validar entrada
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 2. Crear DTO
        dto = LogoutDTO(
            refresh_token=serializer.validated_data['refresh_token']
        )
        
        # 3. Inyectar dependencias
        token_service = JWTTokenService()
        
        # 4. Ejecutar caso de uso
        use_case = LogoutUserUseCase(token_service)
        
        try:
            use_case.execute(dto)
            
            return Response(
                {'message': 'Sesión cerrada exitosamente'},
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ProfileView(APIView):
    """
    Vista para obtener el perfil del usuario autenticado
    
    GET /api/auth/profile/
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    
    def get(self, request):
        # 1. Obtener ID del usuario autenticado
        user_id = request.user.id
        
        # 2. Inyectar dependencias
        user_repository = DjangoUserRepository()
        
        # 3. Ejecutar caso de uso
        use_case = GetUserProfileUseCase(user_repository)
        
        try:
            result = use_case.execute(user_id)
            
            # 4. Serializar respuesta
            response_serializer = UserResponseSerializer(result)
            
            return Response(
                {
                    'data': response_serializer.data
                },
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )


class ProtectedExampleView(APIView):
    """
    Vista de ejemplo protegida
    
    GET /api/auth/protected/
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    
    def get(self, request):
        return Response({
            'message': f'¡Hola {request.user.name}! Esta es una ruta protegida.',
            'user_id': request.user.id,
            'email': request.user.email
        })


class PublicExampleView(APIView):
    """
    Vista de ejemplo pública
    
    GET /api/auth/public/
    """
    permission_classes = (AllowAny,)
    
    def get(self, request):
        return Response({
            'message': 'Esta es una ruta pública, no requiere autenticación.'
        })