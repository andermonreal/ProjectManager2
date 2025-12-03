"""
apps/users/presentation/views.py

Views - Capa de presentación
Maneja peticiones HTTP y delega a los casos de uso
"""


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    RegisterUserSerializer,
    LoginUserSerializer,
    LogoutSerializer,
    AuthTokensSerializer,
    UpdateUserSerializer,
    UserResponseSerializer
)
from ..application.dtos import RegisterUserDTO, LoginUserDTO, LogoutDTO, UpdateUserDTO
from ..application.use_cases.register_user import RegisterUserUseCase
from ..application.use_cases.login_user import LoginUserUseCase
from ..application.use_cases.logout_user import LogoutUserUseCase
from ..application.use_cases.get_user_profile import GetUserProfileUseCase
from ..application.use_cases.update_user import UpdateUserUseCase
from ..infrastructure.repositories import DjangoUserRepository
from ..infrastructure.security import DjangoPasswordHasher, JWTTokenService


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        dto = RegisterUserDTO(
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            phone=serializer.validated_data['phone'],
            birthday=serializer.validated_data['birthday'],
            icon=serializer.validated_data.get('icon')
        )
        
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        use_case = RegisterUserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            result = use_case.execute(dto)
            response_serializer = AuthTokensSerializer(result)
            
            return Response(
                {
                    'message': 'Usuario registrado exitosamente',
                    'data': response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        dto = LoginUserDTO(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        use_case = LoginUserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            result = use_case.execute(dto)
            response_serializer = AuthTokensSerializer(result)
            
            return Response(
                {
                    'message': 'Login exitoso',
                    'data': response_serializer.data
                },
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        dto = LogoutDTO(
            refresh_token=serializer.validated_data['refresh_token']
        )
        
        token_service = JWTTokenService()
        use_case = LogoutUserUseCase(token_service)
        
        try:
            use_case.execute(dto)
            return Response(
                {'message': 'Sesión cerrada exitosamente'},
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        user_id = request.user.id
        user_repository = DjangoUserRepository()
        use_case = GetUserProfileUseCase(user_repository)
        
        try:
            result = use_case.execute(user_id)
            response_serializer = UserResponseSerializer(result)
            
            return Response(
                {'data': response_serializer.data},
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)


class ProtectedExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        return Response({
            'message': f'¡Hola {request.user.name}! Esta es una ruta protegida.',
            'user_id': request.user.id,
            'email': request.user.email
        })


class PublicExampleView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self, request):
        return Response({
            'message': 'Esta es una ruta pública, no requiere autenticación.'
        })

class UpdateUserView(APIView):
    """
    Vista para actualizar datos del usuario autenticado
    
    PATCH /api/auth/profile/update/
    
    Campos modificables:
    - name: Nombre del usuario
    - phone: Teléfono
    - icon: URL del avatar/icono
    - new_password: Nueva contraseña (requiere current_password)
    """
    permission_classes = (IsAuthenticated,)
    
    def patch(self, request):
        # 1. Validar entrada
        serializer = UpdateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 2. Crear DTO
        dto = UpdateUserDTO(
            user_id=request.user.id,
            name=serializer.validated_data.get('name'),
            phone=serializer.validated_data.get('phone'),
            icon=serializer.validated_data.get('icon'),
            current_password=serializer.validated_data.get('current_password'),
            new_password=serializer.validated_data.get('new_password')
        )
        
        # 3. Inyectar dependencias
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        
        # 4. Ejecutar caso de uso
        use_case = UpdateUserUseCase(
            user_repository,
            password_hasher
        )
        
        try:
            result = use_case.execute(dto)
            
            # 5. Serializar respuesta
            response_serializer = UserResponseSerializer(result)
            
            return Response(
                {
                    'message': 'Usuario actualizado exitosamente',
                    'data': response_serializer.data
                },
                status=status.HTTP_200_OK
            )
            
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )