"""
apps/authentication/presentation/urls.py
"""

from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    ProtectedExampleView,
    PublicExampleView
)

urlpatterns = [
    # Autenticación
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Usuario
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Ejemplos
    path('protected/', ProtectedExampleView.as_view(), name='protected'),
    path('public/', PublicExampleView.as_view(), name='public'),
]