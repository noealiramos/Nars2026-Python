# ENTREGABLE SPRINT 3: MENÚ INTERACTIVO

# TODO 1: Importa el módulo random hasta arriba del archivo.


# TODO 2: Crea una variable 'operaciones = 0' fuera del bucle.
# Esta variable debe sobrevivir entre vueltas y contar cuántas operaciones
# útiles realizó el usuario.


# TODO 3: Abre un bucle infinito con 'while True:'.
# Dentro del bucle, imprime un menú con exactamente estas 4 opciones,
# cada una en su propia línea:
#   1. Lanzar dado
#   2. Generar número aleatorio (1-100)
#   3. Ver contador de operaciones
#   4. Salir


# TODO 4: Lee la opción del usuario con input() y guárdala como string
# (NO la conviertas a int — así no se rompe si escribe letras).


# TODO 5: Usa if/elif/else para decidir qué hacer con cada opción:
#   - "1": genera un dado con random.randint(1, 6), imprímelo
#     y suma 1 a 'operaciones'.
#   - "2": genera un número con random.randint(1, 100), imprímelo
#     y suma 1 a 'operaciones'.
#   - "3": imprime el valor actual de 'operaciones'.
#     (NO suma — solo es consulta.)
#   - "4": imprime un mensaje de despedida con el total final
#     de operaciones y usa break para salir del bucle.
#   - Cualquier otro valor (else): imprime un mensaje de opción inválida.
#     El bucle debe volver a mostrar el menú automáticamente.


# TODO 6: Fuera del bucle, imprime un mensaje final como
# "Programa terminado.".

# ENTREGABLE SPRINT 3: MENÚ INTERACTIVO

import random

operaciones = 0

while True:
    print("\n1. Lanzar dado")
    print("2. Generar número aleatorio (1-100)")
    print("3. Ver contador de operaciones")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        dado = random.randint(1, 6)
        print(f"Resultado del dado: {dado}")
        operaciones += 1

    elif opcion == "2":
        numero = random.randint(1, 100)
        print(f"Número aleatorio: {numero}")
        operaciones += 1

    elif opcion == "3":
        print(f"Operaciones realizadas: {operaciones}")

    elif opcion == "4":
        print(f"Hasta luego. Total de operaciones: {operaciones}")
        break

    else:
        print("Opción inválida. Elige entre 1 y 4.")

print("Programa terminado.")