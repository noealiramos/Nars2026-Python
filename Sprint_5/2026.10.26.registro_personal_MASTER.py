# Registro de personal - Operaciones 1: Alta y 2: Listado
# Cada empleado se guarda como un diccionario dentro de esta lista global.
registro = []

def funcion_alta():
    # Captura los datos de un empleado y lo agrega al registro global.
    nombre = input("Nombre del empleado: ")
    departamento = input("Departamento: ")

    # Repetir la captura si el salario no se puede convertir a float.
    while True:
        try:
            salario_mensual = float(input("Salario mensual: "))
            break
        except ValueError:
            print("Ingresa un salario numérico, por ejemplo: 45000.50.")

    # El nivel de acceso debe ser un entero entre 1 y 5.
    while True:
        try:
            nivel_acceso = int(input("Nivel de acceso (1-5): "))
            if 1 <= nivel_acceso <= 5:
                break
            print("El nivel de acceso debe estar entre 1 y 5.")
        except ValueError:
            print("Ingresa un número entero entre 1 y 5.")

    empleado = {
        "nombre": nombre,
        "departamento": departamento,
        "salario_mensual": salario_mensual,
        "nivel_acceso": nivel_acceso,
    }

    registro.append(empleado)
    print(f"Empleado registrado correctamente: {empleado}")


def funcion_listado():
    # Si no hay expedientes, avisar y terminar la función.
    if not registro:
        print("No hay empleados registrados")
        return

    # El contador empieza en 1 y aumenta por cada empleado mostrado.
    numero = 1
    for empleado in registro: #para barrer la lista de registros
        print(f"Empleado {numero}")
        # items() permite recorrer cada clave y su valor en el diccionario.
        for campo, valor in empleado.items(): #items es importante para poder tener el campo / valor
            print(f"  {campo}: {valor}") #al campo le podemos llamar "llave"
        print()
        numero = numero + 1 # lo mismo hace "numero +=1" (en ese orden)


def funcion_menu():
    # El menú se repite hasta que el usuario elija salir.
    while True:
        print("\n=== Menú de registro de personal ===")
        print("1. Alta de usuarios")
        print("2. Consulta de usuarios (listado)")
        print("3. Búsqueda de usuarios por nombre")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            print("\n=== Alta de usuarios ===")
            while True:
                funcion_alta()

                while True:
                    agregar_otro = input("¿Agregar otro? (Y/N): ").strip().upper()
                    if agregar_otro in ("Y", "N"):
                        break
                    print("Responde Y o N.")

                if agregar_otro == "N":
                    break

            print(f"Total de empleados registrados: {len(registro)}")

        elif opcion == "2":
            print("\n=== Consulta de usuarios ===")
            funcion_listado()

        elif opcion == "3":
            # Aquí agregaremos la operación 3 del requerimiento.
            print("Búsqueda por nombre pendiente de implementar.")

        elif opcion == "4":
            print("Hasta luego.")
            break

        else:
            print("Opción inválida. Selecciona un número del 1 al 4.")


funcion_menu()
