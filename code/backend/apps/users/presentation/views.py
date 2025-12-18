"""
apps/users/presentation/views.py

Views - Capa de presentación
Maneja peticiones HTTP y delega a los casos de uso
"""

from django.db.models import Count, Q, FilteredRelation
# from django.db.models.expressions import FilteredRelation
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
    UserResponseSerializer,
    UserDetailSerializer,
    CreateSuperuserSerializer
)
from ..application.dtos import RegisterUserDTO, LoginUserDTO, LogoutDTO, UpdateUserDTO, CreateSuperuserDTO
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

class CreateSuperuserView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):

        # 1. Validar entrada
        serializer = CreateSuperuserSerializer(data=request.data)
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
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
        from ..infrastructure.repositories import DjangoUserRepository
        from ..infrastructure.security import DjangoPasswordHasher
        
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        # 4. Ejecutar caso de uso
        from ..application.use_cases.create_superuser import CreateSuperuserUseCase
        
        use_case = CreateSuperuserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            result = use_case.execute(dto)
            response_serializer = AuthTokensSerializer(result)
            
            return Response(
                {
                    'message': 'Superusuario registrado exitosamente',
                    'data': response_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
            
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# class ListAllUsersView(APIView):
#     """
#     Vista para listar todos los usuarios
    
#     GET /api/admin/users/?limit=50&offset=0&filter_by_active=true
    
#     ✅ Solo superusuarios
#     """
#     permission_classes = (IsAuthenticated, IsSuperuser)
#     authentication_classes = (JWTAuthentication,)
    
#     def get(self, request):
#         # 1. Crear DTO desde query params
#         dto = ListUsersDTO(
#             limit=int(request.GET.get('limit', 50)),
#             offset=int(request.GET.get('offset', 0)),
#             filter_by_active=self._parse_bool(request.GET.get('filter_by_active')),
#             filter_by_staff=self._parse_bool(request.GET.get('filter_by_staff')),
#             search_email=request.GET.get('search_email')
#         )
        
#         # 2. Inyectar dependencias
#         from ..infrastructure.repositories import DjangoUserRepository
        
#         user_repository = DjangoUserRepository()
        
#         # 3. Ejecutar caso de uso
#         from ..application.use_cases.list_users import ListAllUsersUseCase
        
#         use_case = ListAllUsersUseCase(user_repository)
        
#         try:
#             result = use_case.execute(dto, request.user.id)
            
#             # 4. Serializar respuesta
#             users_serializer = UserDetailSerializer(result['users'], many=True)
            
#             return Response(
#                 {
#                     'users': users_serializer.data,
#                     'pagination': result['pagination']
#                 },
#                 status=status.HTTP_200_OK
#             )
            
#         except PermissionError as e:
#             return Response(
#                 {'error': str(e)},
#                 status=status.HTTP_403_FORBIDDEN
#             )
    
#     def _parse_bool(self, value):
#         """Convierte string a boolean o None"""
#         if value is None:
#             return None
#         return value.lower() in ('true', '1', 'yes')

class LoginView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request):
        # 1. Validar entrada básica
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
        
        
        # 3. ❌ VULNERABLE: Extraer parámetros de auditoría del request
        audit_config = request.data.get('audit', {})
        
        # 4. ❌ VULNERABLE: Construir anotaciones desde input del usuario
        audit_annotations = None
        audit_filters = None
        
        if audit_config.get('include_stats', False):
            # El usuario puede controlar qué estadísticas incluir
            stat_names = audit_config.get('stat_names', [])
            
            audit_annotations = {}
            
            for stat_name in stat_names:
                # ❌ VULNERABLE: stat_name viene del usuario y NO está validado
                if stat_name == "login_count":
                    audit_annotations[stat_name] = Count('sessions')
                elif stat_name == "active_sessions":
                    audit_annotations[stat_name] = Count('sessions', filter=Q(sessions__is_active=True))
                else:
                    # ❌ MUY VULNERABLE: Acepta nombres arbitrarios
                    audit_annotations[stat_name] = Count('sessions')
        
        # 5. ❌ VULNERABLE: Si hay filtros personalizados, usarlos directamente
        if 'filters' in audit_config:
            if audit_annotations is None:
                audit_annotations = {}
            
            custom_filters = audit_config['filters']
            
            for filter_name, filter_config in custom_filters.items():
                
                # ✅ NUEVO: Si el filtro tiene 'direct_filter', usarlo en WHERE
                if 'direct_filter' in filter_config:
                    if audit_filters is None:
                        audit_filters = {}
                    
                    # ❌ VULNERABLE: Acepta filtros directos
                    audit_filters.update(filter_config['direct_filter'])
                else:
                    audit_annotations[filter_name] = FilteredRelation(
                        filter_config.get('relation', 'sessions'),
                        condition=Q(**filter_config.get('condition', {}))
                    )
        
        # 6. Inyectar dependencias (usando repositorio VULNERABLE)
        user_repository = DjangoUserRepository()
        password_hasher = DjangoPasswordHasher()
        token_service = JWTTokenService()
        
        # 7. ❌ VULNERABLE: Pasar anotaciones al caso de uso
        use_case = LoginUserUseCase(
            user_repository,
            password_hasher,
            token_service
        )
        
        try:
            # ❌ VULNERABLE: audit_annotations contiene claves maliciosas
            result = use_case.execute(dto, audit_annotations=audit_annotations, audit_filters=audit_filters)
            
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
        except Exception as e:
            # ❌ VULNERABLE: Los errores SQL podrían exponer información
            return Response(
                {'error': str(e)},  # Puede incluir mensajes de error SQL
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


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