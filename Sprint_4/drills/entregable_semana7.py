# GESTOR DE TAREAS V2

# Lista global que conserva las tareas durante la sesión.
tareas = []


def agregar_tarea():
    tarea = input("Escribe la tarea que deseas agregar: ").strip()

    if tarea == "":
        print("La tarea no puede estar vacía.")
    elif tarea in tareas:
        print("Esa tarea ya existe.")
    else:
        tareas.append(tarea)
        print(f"Tarea agregada: {tarea}")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\n=== TAREAS REGISTRADAS ===")
        for numero, tarea in enumerate(tareas, start=1):
            print(f"{numero}. {tarea}")


def eliminar_tarea():
    tarea = input("Escribe la tarea que deseas eliminar: ").strip()

    if tarea not in tareas:
        print("Esa tarea no existe.")
    else:
        tareas.remove(tarea)
        print(f"Tarea eliminada: {tarea}")


def buscar_tarea():
    tarea = input("Escribe la tarea que deseas buscar: ").strip()

    if tarea in tareas:
        print(f"Tarea encontrada: {tarea}")
    else:
        print("Esa tarea no existe.")


def mostrar_primeras_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    try:
        n = int(input("¿Cuántas tareas deseas mostrar? "))
    except ValueError:
        print("Ingresa un número entero válido.")
        return

    if n <= 0:
        print("La cantidad debe ser mayor que cero.")
    else:
        primeras_tareas = tareas[:n]

        print(f"\n=== PRIMERAS {n} TAREAS (O LAS DISPONIBLES) ===")
        for numero, tarea in enumerate(primeras_tareas, start=1):
            print(f"{numero}. {tarea}")


# Menú principal.
while True:
    print("\n=== GESTOR DE TAREAS V2 ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Buscar tarea")
    print("5. Mostrar primeras N tareas")
    print("6. Salir")

    opcion = input("Selecciona una opción (1-6): ").strip()

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        buscar_tarea()
    elif opcion == "5":
        mostrar_primeras_tareas()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Selecciona una opción del 1 al 6.")