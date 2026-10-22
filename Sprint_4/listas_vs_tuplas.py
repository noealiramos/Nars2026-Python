# COMPARACIÓN: LISTAS VS TUPLAS

# ===== PARTE 1: LISTAS (modificables) =====

# TODO 1: Mostrar encabezado.
print("=== LISTAS (Modificables) ===")

# TODO 2: Crear la lista inicial.
tareas = ["estudiar", "ejercicio", "compras"]
print(f"Lista inicial: {tareas}")

# TODO 3: Agregar una tarea.
tareas.append("leer")
print(f"Después de agregar 'leer': {tareas}")

# TODO 4: Reemplazar el elemento del índice 1.
tareas[1] = "yoga"
print(f"Después de cambiar 'ejercicio' por 'yoga': {tareas}")

# TODO 5: Eliminar 'compras'.
tareas.remove("compras")
print(f"Después de quitar 'compras': {tareas}")


# ===== PARTE 2: TUPLAS (inmutables) =====

# TODO 6: Mostrar encabezado.
print("\n=== TUPLAS (Inmutables) ===")

# TODO 7: Crear la tupla de configuración.
config = ("localhost", 8080, "producción")
print(f"Configuración original: {config}")

# TODO 8: Acceder a cada elemento por índice.
print(f"Servidor: {config[0]}")
print(f"Puerto: {config[1]}")
print(f"Ambiente: {config[2]}")

# TODO 9: Desempaquetar la tupla en una sola línea.
servidor, puerto, ambiente = config
print(f"Desempaque: servidor={servidor}, puerto={puerto}, ambiente={ambiente}")

# TODO 10: Crear una NUEVA tupla con otro puerto.
config_nueva = (config[0], 9000, config[2])
print(f"Configuración nueva: {config_nueva}")
print(f"La configuración original se conserva: {config}")


# ===== PARTE 3: CASOS DE USO =====

# TODO 11: Mostrar encabezado.
print("\n=== CASOS DE USO ===")

# TODO 12: Usar una tupla para las coordenadas de un punto fijo.
ubicacion = (19.4326, -99.1332)
print(f"Ubicación fija (tupla): {ubicacion}")

# TODO 13: Usar una lista para compras que pueden cambiar.
compras = ["leche", "pan"]
compras.append("huevos")
print(f"Lista de compras: {compras}")

# TODO 14: Crear una tupla con los días de la semana.
# El nombre en mayúsculas indica, por convención, una constante.
DIAS = ("Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom")
print(f"Día en el índice 2: {DIAS[2]}")