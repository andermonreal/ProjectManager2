from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
import json
import subprocess
import os

@api_view(['POST'])
@permission_classes([IsAdminUser])
def system_diagnostics(request):
    """
    Panel de diagnóstico del sistema para administradores.
    Permite ejecutar comandos de sistema para verificar salud del servidor.
    """

    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    try:
        data = json.loads(request.body)
        command_type = data.get('command_type')
        
        # ❌ VULNERABLE: Lista blanca insuficiente
        allowed_commands = {
            'disk_usage': 'df -h',
            'memory': 'free -m',
            'processes': 'ps aux',
            'network': 'netstat -tuln',
            'logs': 'tail -n 100',  # ⚠️ Falta validar el archivo
        }
        
        if command_type not in allowed_commands:
            return JsonResponse({'error': 'Comando no permitido'}, status=400)
        
        base_command = allowed_commands[command_type]
        
        # ❌ CRÍTICO: Permite parámetros adicionales sin validar
        if command_type == 'logs':
            log_file = data.get('log_file', '/var/log/syslog')
            
            # ❌ VULNERABILIDAD: Concatenación directa sin sanitizar
            full_command = f"{base_command} {log_file}"
        else:
            full_command = base_command
        
        # ❌ CRÍTICO: shell=True permite command injection
        result = subprocess.run(
            full_command,
            shell=True,  # 🚨 PELIGROSO
            capture_output=True,
            text=True,
            timeout=10
        )
        
        return JsonResponse({
            'success': True,
            'output': result.stdout,
            'error': result.stderr
        })
        
    except subprocess.TimeoutExpired:
        return JsonResponse({'error': 'Comando excedió timeout'}, status=408)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def backup_database(request):
    """
    Crea backup de la base de datos.
    Permite especificar ruta de destino y formato de compresión.
    """
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    try:
        data = json.loads(request.body)
        
        # ❌ VULNERABLE: Permite rutas arbitrarias
        backup_path = data.get('backup_path', '/tmp/backup.sql')
        compression = data.get('compression', 'none')  # none, gzip, bzip2
        
        # ❌ CRÍTICO: No valida caracteres peligrosos en backup_path
        # ❌ CRÍTICO: No valida que compression sea un valor válido
        
        if compression == 'none':
            # ❌ VULNERABLE: f-string con input del usuario
            command = f"pg_dump mydb > {backup_path}"
        else:
            # ❌ VULNERABLE: Permite inyectar comandos via compression
            command = f"pg_dump mydb | {compression} > {backup_path}"
        
        # ❌ CRÍTICO: shell=True + input no sanitizado = RCE
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        return JsonResponse({
            'success': True,
            'message': f'Backup creado en {backup_path}',
            'output': result.stdout
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)