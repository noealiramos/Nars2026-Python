# incidentManager.py
# Sistema de gestión de incidentes v1 - Sprint 4 · Clase 7
# Mesa de servicio en memoria: registrar, listar, cerrar y buscar incidentes.

incidentes = [
    "TKT-001: usuario no puede ingresar al portal de nómina",
    "TKT-002: impresora del piso 4 sin conexión",
    "TKT-003: cliente reporta cargo duplicado",
]

while True:
    print("\n=== GESTOR DE INCIDENTES ===")
    print("1. Registrar nuevo incidente")
    print("2. Listar incidentes abiertos")
    print("3. Cerrar incidente")
    print("4. Buscar incidente por ID")
    print("5. Salir")

    opcion = input("\nElige una opción (1-5): ")

    if opcion == "1":
        nuevo = input("Describe el incidente (incluye ID): ").strip()
        if nuevo:
            incidentes.append(nuevo)
            print(f"Incidente registrado. Total abiertos: {len(incidentes)}")
        else:
            print("Descripción vacía, no se registró.")

    elif opcion == "2":
        if len(incidentes) == 0:
            print("No hay incidentes abiertos.")
        else:
            print("\n--- INCIDENTES ABIERTOS ---")
            for i in range(len(incidentes)):
                print(f"{i + 1}. {incidentes[i]}")
            print(f"Total: {len(incidentes)}")

    elif opcion == "3":
        if len(incidentes) == 0:
            print("No hay incidentes para cerrar.")
        else:
            numero = input("Número de incidente a cerrar: ")
            if numero.isdigit():
                pos_humana = int(numero)
                if pos_humana >= 1 and pos_humana <= len(incidentes):
                    cerrado = incidentes.pop(pos_humana - 1)
                    print(f"Incidente cerrado: {cerrado}")
                else:
                    print(f"Número fuera de rango. Hay {len(incidentes)} incidentes.")
            else:
                print("Debe ser un número.")

    elif opcion == "4":
        consulta = input("ID a buscar (ej. TKT-001): ").strip()
        encontrado = False
        for ticket in incidentes:
            if consulta in ticket:
                print(f"Encontrado: {ticket}")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ese ID.")

    elif opcion == "5":
        print("Sesión cerrada. Hasta el próximo turno.")
        break

    else:
        print("Opción inválida. Elige del 1 al 5.")
