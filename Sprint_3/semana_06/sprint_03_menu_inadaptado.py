# REQUERIMIENTOS OBLIGATORIOS (para sprint_03)
# Archivo guardado como menu_inadaptado.py en clase-06/

# El menú muestra EXACTAMENTE estas 4 opciones, numeradas:
# Crear
# Ver lista
# Actualizar
# Salir

# Motor while True: como único bucle del programa

# Validación de opción inválida con continue (mensaje + volver al menú)

# Opciones 1, 2, 3 muestran mensaje placeholder:"--- [Función] en construcción ---" (area de texto donde va a ir cierto valor / función)

# Opción 4 muestra "Cerrando aplicación..." y termina con break
# Comparaciones del input como strings ("1", "2", "3", "4")
# UN SOLO break en todo el archivo, exclusivamente en la opción 4

# CRITERIOS DE VERIFICACIÓN (correr el programa y validar):
# ☐ ¿El programa sigue corriendo después de elegir 1, 2 o 3?
# ☐ ¿El programa termina limpiamente solo con la opción 4?
# ☐ ¿Una letra (ej. "hola") muestra el mensaje de error y vuelve al menú?
# ☐ ¿Un número fuera de rango (ej. "9") muestra el mensaje de error y vuelve al menú?
# ☐ ¿Enter en blanco muestra el mensaje de error y vuelve al menú?
# ☐ ¿La opción inválida usa continue (NO break)?
# ☐ ¿Está el break únicamente en la opción 4?

#lo vamos a aplicar

# sprint_03
# Archivo: menu_inadaptado.py

while True:
    print("\n--- MENÚ ---")
    print("1. Crear")
    print("2. Ver lista")
    print("3. Actualizar")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    # Validación de opción inválida
    if opcion not in ("1", "2", "3", "4"):
        print("Opción inválida. Intenta nuevamente.")
        continue

    if opcion == "1":
        print("--- Funcion Crear en construcción ---")

    elif opcion == "2":
        print("--- Funcion Ver lista en construcción ---")

    elif opcion == "3":
        print("--- Funcion Actualizar en construcción ---")

    elif opcion == "4":
        print("Cerrando aplicación...")
        break