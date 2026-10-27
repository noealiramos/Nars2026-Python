
# CONTEXTO: Expediente digital de empleado

# FASE 1: Crear expediente
empleado = {
    "nombre": "ana garcia",
    "departamento": "finanzas",
    "salario_mensual": 45000.00,
    "nivel_acceso": 4,
    "activo": "si"
}

print(empleado)

# FASE 2: Leer campos específicos
print("Empleado:", empleado["nombre"])
print("Salario actual:", empleado["salario_mensual"])

# FASE 3: Actualizar salario
# A Ana le subieron el sueldo un 10%
empleado["salario_mensual"] = empleado["salario_mensual"] * 1.10

print("Salario tras aumento:", empleado["salario_mensual"])

# FASE 4: Agregar un campo nuevo
empleado["fecha_revision"] = "2026-10"

print(empleado)

#fase 3: guardia de entada - preguntar ANTES de leer
campo = input("¿que campo requieres consultar?")

if campo in empleado:
    print(f"{campo}:{empleado[campo]}")
else:
    print(f"este expediente no tiene el campo '{campo}',")
    
#alternativa profesional con get()
print("telefono registado: ", empleado.get("telefono", "noregistrado"))

#trarnos todos los valores, de todas las llaves que tiene el problema ► a través de un "for"
for elemento in empleado:
    print(elemento)
    
#convertir una lista si necesito indezar o contar
lista_campo = list(empleado.keys())
print("total de cmapos:")