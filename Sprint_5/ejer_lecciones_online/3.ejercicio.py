# Base de datos de un recluta
recluta = {
    "nombre": "Carlos Ruiz",
    "edad": 22,
    "rango": "Novato",
    "puntos": 150
}

# Consultar datos
print(f"Nombre: {recluta['nombre']}")
print(f"Rango: {recluta['rango']}")

# Actualizar datos (subir puntos)
recluta["puntos"] += 50
print(f"Nuevos puntos: {recluta['puntos']}")  # 200

# Agregar nuevo campo
recluta["especialidad"] = "Python"