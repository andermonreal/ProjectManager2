from django.urls import path
from .views import system_diagnostics, backup_database

urlpatterns = [
    path('diagnostics', system_diagnostics, name='diagnostics'),
    path('backup', backup_database, name='backup'),
]