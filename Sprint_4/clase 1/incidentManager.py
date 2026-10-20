
# ==================================================
# INCIDENT MANAGER - SISTEMA DE MESA DE SERVICIO
# ==================================================

# Lista inicial con 3 incidentes pendientes
incidentes = ["INC001", "INC002", "INC003"]

# Menu principal
while True:
    print("\n===== INCIDENT MANAGER =====")
    print("1. Registrar nuevo incidente")
    print("2. Listar todos los incidentes abiertos")
    print("3. Cerrar un incidente")
    print("4. Buscar incidente por ID")
    print("5. Salir del sistema")

    opcion = input("\nSelecciona una opcion (1-5): ")

    # OPCION 1: REGISTRAR INCIDENTE
    if opcion == "1":
        print("\n--- Registrar incidente ---")
        nuevo_id = input("Ingresa el ID del incidente: ").strip()

        if nuevo_id == "":
            print("El ID no puede estar vacio.")

        elif nuevo_id in incidentes:
            print("Este incidente ya existe.")

        else:
            incidentes.append(nuevo_id)
            print("Incidente registrado correctamente.")

    # OPCION 2: LISTAR INCIDENTES
    elif opcion == "2":
        print("\n--- Incidentes abiertos ---")

        if len(incidentes) == 0:
            print("No hay incidentes abiertos.")

        else:
            for i in range(len(incidentes)):
                print(f"{i + 1}. {incidentes[i]}")

            print(f"Total de incidentes: {len(incidentes)}")

    # OPCION 3: CERRAR INCIDENTE
    elif opcion == "3":
        print("\n--- Cerrar incidente ---")

        if len(incidentes) == 0:
            print("No hay incidentes abiertos.")

        else:
            for i in range(len(incidentes)):
                print(f"{i + 1}. {incidentes[i]}")

            numero = input(
                "\nNumero del incidente a cerrar: "
            )

            if numero.isdigit():
                numero = int(numero)

                if 1 <= numero <= len(incidentes):
                    indice = numero - 1
                    cerrado = incidentes.pop(indice)

                    print(f"Incidente {cerrado} cerrado correctamente.")

                else:
                    print(
                        f"Numero fuera de rango. "
                        f"Hay {len(incidentes)} incidentes."
                    )

            else:
                print("Debes ingresar un numero valido.")

    # OPCION 4: BUSCAR INCIDENTE
    elif opcion == "4":
        print("\n--- Buscar incidente ---")

        buscar_id = input(
            "Ingresa el ID exacto del incidente: "
        ).strip()

        if buscar_id in incidentes:
            print("Encontrado")
        else:
            print("No se encontró ese ID.")

    # OPCION 5: SALIR
    elif opcion == "5":
        print("Sesión cerrada. Hasta el próximo turno.")
        break

    # OPCION INVALIDA
    else:
        print("Opción inválida")
