#reto utiliando funciones definidas con def, minimo 3 funciones

# INICIO  ·  tareas = []  ·  OPCIONES_VALIDAS = ("1".."6")
# while True:
#  ├─ mostrar_menu()  ·  opcion = input()
#  ├─ "1" → texto = input() → tareas.append(texto)
#  ├─ "2" → listar_tareas(tareas)
#  ├─ "3" → numero = int(input())  →  indice = numero - 1
#  │        ├─ if 0 <= indice < len(tareas): tareas.pop(indice)
#  │        └─ else: "Esa tarea no existe"
#  ├─ "4" → for t in sorted(tareas): print(t)   (original intacto)
#  ├─ "5" → resumen(tareas, 4)
#  ├─ "6" → break → FIN
#  └─ else → "Opción no válida"

#  gestor con menú while True, ≥3 mini-funciones, 
#  lista dinámica, ordenamiento bajo demanda, métrica con math, 
#  y validación de índice. 
#  El QA prueba 11 casos. 
#  Qué NO busca: no se usa try/except (Sprint 6) — robustez con if+len(). '''

import math

# === VARIABLES GLOBALES ===

tareas = []
OPCIONES_VALIDAS = ("1", "2", "3", "4", "5", "6")

# === FUNCION 1: MOSTRAR MENU ===

def mostrar_menu():
    print("\n====GESTOR DE TAREAS ===")
    print("1. agregar tarea")
    print("2. listar tareas")
    print("3. eliminar tarea")
    print("4. ordenar tareas")
    print("5. resumen de tareas")
    print("6. Salir")


# === FUNCION 2: LISTAR TAREAS ===

def listar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas registradas.")
    else:
        print("\n=== LISTA DE TAREAS ===")
        for i in range(len(tareas)):
            print(f"{i + 1}. {tareas[i]}")


# === FUNCION 3: AGREGAR TAREA ===

def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ")

    if len(texto.strip()) > 0:
        tareas.append(texto)
        print("Tarea agregada correctamente.")
    else:
        print("La tarea no puede estar vacia.")


# === FUNCION 4: ELIMINAR TAREA ===

def eliminar_tarea(tareas):
    listar_tareas(tareas)

    if len(tareas) == 0:
        return

    numero = input("Numero de tarea a eliminar: ")

    if numero.isdigit():
        indice = int(numero) - 1

        if 0 <= indice < len(tareas):
            eliminada = tareas.pop(indice)
            print(f"Tarea eliminada: {eliminada}")
        else:
            print("Esa tarea no existe.")
    else:
        print("Debes ingresar un numero valido.")


# === FUNCION 5: RESUMEN ===

def resumen(tareas, capacidad):
    total = len(tareas)
    bloques = math.ceil(total / capacidad)

    print("\n=== RESUMEN DE TAREAS ===")
    print(f"Total de tareas: {total}")
    print(f"Capacidad por bloque: {capacidad}")
    print(f"Bloques necesarios: {bloques}")


# === PROGRAMA PRINCIPAL ===

while True:

    mostrar_menu()
    opcion = input("Selecciona una opcion (1-6): ")

    if opcion not in OPCIONES_VALIDAS:
        print("Opcion no valida.")

    elif opcion == "1":
        agregar_tarea(tareas)

    elif opcion == "2":
        listar_tareas(tareas)

    elif opcion == "3":
        eliminar_tarea(tareas)

    elif opcion == "4":
        print("\n=== TAREAS ORDENADAS ===")

        for tarea in sorted(tareas):
            print(tarea)

    elif opcion == "5":
        resumen(tareas, 4)

    elif opcion == "6":
        print("Saliendo del gestor de tareas...")
        break
