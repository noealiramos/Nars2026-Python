# GESTOR DE TAREAS — SonidoLibre
# Organiza las tareas del festival con listas, tuplas y una función de reporte.

# TODO 1: Lista con al menos 5 tareas pendientes.
tareas = [
    "montar escenario principal",
    "revisar sistema de sonido",
    "confirmar bandas",
    "organizar accesos",
    "preparar camerinos"
]

# TODO 2: Tupla con la configuración del festival.
config_festival = ("SonidoLibre", 2026, 2000, "Aguascalientes")

# TODO 3: Imprimir la configuración usando tuple unpacking.
nombre, anio, capacidad, ciudad = config_festival

print(
    f"Festival: {nombre} {anio} | "
    f"Capacidad: {capacidad} | Ciudad: {ciudad}"
)

# TODO 4: Agregar 2 tareas y eliminar la primera.
tareas.append("instalar iluminación")
tareas.append("coordinar seguridad")

tarea_eliminada = tareas.pop(0)
print(f"\nTarea eliminada: {tarea_eliminada}")

# TODO 5: Ordenar con sorted() y verificar la lista original.
tareas_antes = tareas.copy()

print("\n===== TAREAS ORDENADAS =====")
print(sorted(tareas))

print("\n===== LISTA ORIGINAL =====")
print(tareas)

print(f"\n¿La lista original NO cambió? {tareas == tareas_antes}")


# TODO 6: Función sin parámetros que imprime el reporte.
def mostrar_reporte():
    print("\n===== REPORTE DE TAREAS =====")
    print(f"Total de tareas: {len(tareas)}")

    for tarea in tareas:
        print(f"→ {tarea}")


# Llamada a la función al final.
mostrar_reporte()