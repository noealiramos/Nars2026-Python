# BASE DE RECLUTAS · INADAPTADOS
# Base de talento con menu de 4 opciones.
# Cada recluta es un diccionario con 5 campos:
#   nombre, area, salario_mensual, estatus, email

# Lista de arranque (ya poblada con 3 reclutas).
base_reclutas = [
    {"nombre": "Ana Torres",    "area": "Finanzas",  "salario_mensual": 28500.0,  "estatus": "activo",   "email": "ana.torres@inadaptados.mx"},
    {"nombre": "Luis Quintero", "area": "Logistica", "salario_mensual": 19200.0,  "estatus": "activo",   "email": "luis.quintero@inadaptados.mx"},
    {"nombre": "Mara Ibarra",   "area": "Salud",     "salario_mensual": 133750.0, "estatus": "inactivo", "email": "mara.ibarra@inadaptados.mx"},
]

# Menu con while True (patron del Sprint 3).
while True:
    print()
    print("=== BASE DE RECLUTAS · INADAPTADOS ===")
    print("1) Alta de recluta")
    print("2) Listado (reporte)")
    print("3) Buscar por nombre")
    print("4) Salir")
    opcion = input("Elige una opcion: ").strip()

    # 1) Alta: captura cada campo REASIGNANDO la limpieza.
    if opcion == "1":
        nombre = input("Nombre: ")
        nombre = nombre.strip().title()

        area = input("Area: ")
        area = area.strip().title()

        salario_mensual = float(input("Salario mensual: ").strip())

        estatus = input("Estatus (activo/inactivo): ")
        estatus = estatus.strip().lower()

        email = input("Email: ")
        email = email.strip().lower()

        recluta = {
            "nombre": nombre,
            "area": area,
            "salario_mensual": salario_mensual,
            "estatus": estatus,
            "email": email,
        }
        base_reclutas.append(recluta)
        print(f"[OK] Recluta '{nombre}' registrado. Total: {len(base_reclutas)}")

    # 2) Listado: reporte tabular con 4 columnas.
    elif opcion == "2":
        print()
        print(f"{'NOMBRE':<18}{'AREA':<14}{'ESTATUS':<11}{'SALARIO':>14}")
        print("-" * 57)
        for recluta in base_reclutas:
            print(f"{recluta['nombre']:<18}"
                  f"{recluta['area']:<14}"
                  f"{recluta['estatus']:<11}"
                  f"{recluta['salario_mensual']:>14,.2f}")
        print("-" * 57)
        print(f"Total de reclutas: {len(base_reclutas)}")

    # 3) Buscar: coincidencia parcial sin importar mayusculas.
    elif opcion == "3":
        termino = input("Nombre a buscar: ")
        termino = termino.strip().lower()

        encontrados = 0
        for recluta in base_reclutas:
            if termino in recluta["nombre"].lower():
                print(f"- {recluta['nombre']} | {recluta['area']} | "
                      f"{recluta['estatus']} | ${recluta['salario_mensual']:,.2f} | "
                      f"{recluta['email']}")
                encontrados += 1

        if encontrados == 0:
            print(f"[!] No se encontraron reclutas con '{termino}'.")
        else:
            print(f"Coincidencias: {encontrados}")

    # 4) Salir: despedida y break.
    elif opcion == "4":
        print("Hasta luego, Inadaptado. Base cerrada.")
        break

    # Opcion invalida.
    else:
        print(f"[ERROR] Opcion '{opcion}' no valida. Elige 1, 2, 3 o 4.")