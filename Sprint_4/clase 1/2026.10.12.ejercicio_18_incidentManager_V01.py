incidentes = ["ticket-001", "ticket-002","ticket-003"]

while True:
    print("\n--- MENÚ ---")
    print("1. Registrar nuevo incidente")
    print("2. Listar todos los incidentes abiertos")
    print("3. Cerrar un incidente (por número de posición)")
    print("4. Buscar si un incidente existe (por ID exacto)")
    print("5. Salir del sistema")

    opcion = input("Selecciona una opción: ")

    # Validación de opción inválida
    if opcion not in ("1", "2", "3", "4","5"):
        print("Opción inválida. Intenta nuevamente.")
        continue

    if opcion == "1":
        print("--- Registrar nuevo incidente---")
        ticket_nuevo = input("Ingrese el ID del incidente: ")
        if ticket_nuevo not in incidentes:
            incidentes.append(ticket_nuevo)
            print(f"El incidente {ticket_nuevo} ha sido agregado a la lista.")
        else:
            print(f"El incidente {ticket_nuevo} ya está presente en la lista.")
            
        print(incidentes)

    elif opcion == "2":
        print("--- Listar todos los incidentes abiertos ---")
        print(f"Los tickets abiertos son:  {incidentes}")


    elif opcion == "3":
        print("--- Cerrar un incidente (por número de posición ---")
        ticket_cerrar = input("Ingrese el ID del ticket a cerrar: ")
        
        if ticket_cerrar in incidentes:
            print(f"El ticket {ticket_cerrar} será cerrado / eliminado de  la lista.")
            incidentes.remove(ticket_cerrar)
            print(incidentes)
        else:
            print(f"El ticket {ticket_cerrar} no está presente en la lista.")
            print(incidentes)
   
    elif opcion == "4":
        print("--- Buscar si un incidente existe (por ID exacto) ---")

        ticket_buscar = input("Ingrese el ID del ticket a BUSCAR: ")
        
        if ticket_buscar in incidentes:
            print(f"El ticket {ticket_buscar} SI ESTÁ CONTENIDO EN  la lista.")
            print(incidentes)
        else:
            print(f"El ticket {ticket_buscar} NO ESTÁ CONTENIDO EN  la lista.")
            print(incidentes) 
        
    elif opcion == "5":
        print("Sesión cerrada. Hasta el próximo turno")
        break