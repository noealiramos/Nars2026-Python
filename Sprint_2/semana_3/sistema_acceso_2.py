# CONTEXTO: Sistema de Control de Acceso Corporativo
# Una empresa necesita un script de validación para su sistema de seguridad física.
# El guardia ingresa los datos del empleado y el sistema determina qué nivel de acceso corresponde.

# Variables de entrada:
#   · ID del empleado (texto)
#   · Nivel de acceso asignado (entero 1-5)
#   · Departamento (Tecnología / Finanzas / RRHH / Operaciones / Dirección)
#   · Autorización especial vigente (si/no)
#   · Hora de ingreso (entero 0-23)

# Reglas de negocio (las construiremos en orden):
#   Regla 1: Horario laboral = entre las 8:00 y las 20:00 hrs.
#   Regla 2: Nivel 5 O autorización especial → acceso completo (con registro fuera de horario)
#   Regla 3: Nivel 3-4 en horario en depto. crítico → acceso a área restringida
#   Regla 4: Nivel 2-4 en horario → acceso a área general
#   Regla 5: Cualquier otro caso → acceso denegado

# Archivo: sistema_acceso.py

empleado_id   = input("ID de empleado: ")
nivel_acceso  = int(input("Nivel de acceso (1-5): "))
departamento  = input("Departamento: ")
autorizacion  = input("¿Autorización especial vigente? (si/no): ")
hora_ingreso  = int(input("Hora de ingreso (0-23): "))

en_horario = hora_ingreso >=8 and hora_ingreso <=20 #resultado booleano CORRESPONDEN A FASE #2

# # #Fase 3: Regla de nivel máximo y autorización especial
if nivel_acceso == 5 or autorizacion == "si":
    if en_horario:
        print(f"ACCESO CONCEDIDO — Empleado {empleado_id}: \
            área completa.")
    else:
        print(f"ACCESO FUERA DE HORARIO — Empleado {empleado_id}: \
            acceso completo con registro de alerta.")


#>>>>>>>>>>>>>>>>>>>>> FASE 4

#Fase 4: Acceso restringido por nivel y departamento
elif nivel_acceso >= 3 and en_horario:
    depto_critico = departamento == "Tecnología" \
        or departamento == "Finanzas" or departamento == "Dirección"
    if depto_critico:
        print(f"ACCESO CONCEDIDO — Empleado {empleado_id}: área restringida ({departamento}).")
    else:
        print(f"ACCESO PARCIAL — Empleado {empleado_id}: área general solamente (departamento sin permisos ampliados).")

#>>>>>>>>>>>>>>>>>>>>> FASE 5
