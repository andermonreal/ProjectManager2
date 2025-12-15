# class ListAllUsersUseCase:
#     """
#     Caso de uso: Listar todos los usuarios (solo admin)
    
#     Permite a los superusuarios ver todos los usuarios registrados
#     con filtros y búsqueda
#     """
    
#     def __init__(self, user_repository):
#         self._user_repository = user_repository
    
#     def execute(
#         self, 
#         dto: ListUsersDTO,
#         requesting_user_id: int
#     ) -> dict:
#         """
#         Ejecuta el caso de uso de listar usuarios
        
#         Args:
#             dto: Parámetros de filtrado y paginación
#             requesting_user_id: ID del usuario que hace la petición
            
#         Returns:
#             Dict con lista de usuarios y metadatos de paginación
            
#         Raises:
#             PermissionError: Si el usuario no es superusuario
#         """
#         # 1. Validar entrada
#         dto.validate()
        
#         # 2. Verificar que el usuario que solicita sea superusuario
#         requesting_user = self._user_repository.find_by_id(requesting_user_id)
        
#         if not requesting_user or not requesting_user.is_superuser:
#             raise PermissionError("Solo los superusuarios pueden listar todos los usuarios")
        
#         # 3. Obtener usuarios con filtros
#         users = self._get_filtered_users(dto)
        
#         # 4. Convertir a DTOs
#         user_dtos = [UserResponseDTO.from_entity(user) for user in users]
        
#         # 5. Obtener total para paginación
#         total = self._count_filtered_users(dto)
        
#         # 6. Retornar con metadatos
#         return {
#             'users': user_dtos,
#             'pagination': {
#                 'total': total,
#                 'limit': dto.limit,
#                 'offset': dto.offset,
#                 'has_more': (dto.offset + dto.limit) < total
#             }
#         }
    
#     def _get_filtered_users(self, dto: ListUsersDTO) -> list[UserEntity]:
#         """Obtiene usuarios aplicando filtros"""
#         from infrastructure.models import User
        
#         queryset = User.objects.all()
        
#         # Aplicar filtros
#         if dto.filter_by_active is not None:
#             queryset = queryset.filter(is_active=dto.filter_by_active)
        
#         if dto.filter_by_staff is not None:
#             queryset = queryset.filter(is_staff=dto.filter_by_staff)
        
#         if dto.search_email:
#             queryset = queryset.filter(email__icontains=dto.search_email)
        
#         # Paginación
#         queryset = queryset.order_by('-date_joined')[dto.offset:dto.offset + dto.limit]
        
#         return [user.to_entity() for user in queryset]
    
#     def _count_filtered_users(self, dto: ListUsersDTO) -> int:
#         """Cuenta total de usuarios con filtros"""
#         from infrastructure.models import User
        
#         queryset = User.objects.all()
        
#         if dto.filter_by_active is not None:
#             queryset = queryset.filter(is_active=dto.filter_by_active)
        
#         if dto.filter_by_staff is not None:
#             queryset = queryset.filter(is_staff=dto.filter_by_staff)
        
#         if dto.search_email:
#             queryset = queryset.filter(email__icontains=dto.search_email)
        
#         return queryset.count()