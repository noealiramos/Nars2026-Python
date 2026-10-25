# ENTREGABLE SPRINT 4: GESTOR DE TAREAS V2
# Listas, funciones, ordenamiento, math y validación de índice.

# TODO 1: Importar math.
import math

# TODO 2: Lista global de tareas.
tareas = []

# TODO 3: Tupla de opciones válidas.
OPCIONES_VALIDAS = ("1", "2", "3", "4", "5", "6")


# ===== FUNCIONES =====

# TODO 4: Mostrar las 6 opciones.
def mostrar_menu():
    print("\n===== GESTOR DE TAREAS V2 =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Ordenar A-Z (vista)")
    print("5. Resumen (días mínimos)")
    print("6. Salir")


# TODO 5: Listar las tareas numeradas desde 1.
def listar_tareas(lista):
    if not lista:
        print("No hay tareas registradas.")
    else:
        numero = 1

        for tarea in lista:
            print(f"{numero}. {tarea}")
            numero += 1


# TODO 6: Calcular los días mínimos.
def resumen(lista, por_dia):
    total = len(lista)

    if not lista:
        print("No hay tareas registradas. Días mínimos: 0.")
    else:
        dias = math.ceil(total / por_dia)

        print(f"Total de tareas: {total}")
        print(f"Tareas por día: {por_dia}")
        print(f"Días mínimos necesarios: {dias}")


# ===== MENÚ PRINCIPAL =====

# TODO 7: Repetir el menú hasta elegir salir.
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    # TODO 14: Validar la opción.
    if opcion not in OPCIONES_VALIDAS:
        print("Opción no válida. Elige del 1 al 6.")

    # TODO 8: Agregar una tarea.
    elif opcion == "1":
        texto = input("Escribe la tarea: ").strip()

        if texto:
            tareas.append(texto)
            print(f"Tarea agregada. Total actual: {len(tareas)}")
        else:
            print("La tarea no puede estar vacía.")

    # TODO 9: Listar tareas.
    elif opcion == "2":
        listar_tareas(tareas)

    # TODO 10: Eliminar por número con validación.
    elif opcion == "3":
        if not tareas:
            print("No hay tareas registradas.")
        else:
            listar_tareas(tareas)

            try:
                numero = int(input("Número de la tarea a eliminar: "))
                indice = numero - 1

                if indice >= 0 and indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    print(f"Tarea eliminada: {tarea_eliminada}")
                else:
                    print("Esa tarea no existe.")

            except ValueError:
                print("Debes ingresar un número entero.")

    # TODO 11: Mostrar una vista ordenada sin modificar la lista.
    elif opcion == "4":
        orden_original = tareas.copy()

        print("\n===== TAREAS ORDENADAS A-Z =====")
        listar_tareas(sorted(tareas))

        print(
            "¿La lista original conservó su orden? "
            f"{tareas == orden_original}"
        )

    # TODO 12: Mostrar el resumen con 4 tareas por día.
    elif opcion == "5":
        resumen(tareas, 4)

    # TODO 13: Salir del menú.
    elif opcion == "6":
        print("¡Hasta luego!")
        break