from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth0/', include('modules.auth0.urls')),
    path('api/usuarios/', include('modules.usuarios.urls')),
    path('api/estaciones/', include('modules.estaciones.urls')),
]
