usuario = input("Nombre del usuario: ")
contrasena = input("Contraseña del usuario: ")
ip_origen = input("IP de origen: ")

if usuario == "superadmin":
    red_corporativa = ip_origen.startswith("192.168.")
    if contrasena == "S@perAdmin2024" and red_corporativa:
        print("ACCESO TOTAL — superadmin: todos los módulos habilitados.")
    elif contrasena != "S@perAdmin2024":
        print("DENEGADO — superadmin: contraseña incorrecta.")
    else:
        print("DENEGADO — superadmin: acceso remoto no permitido.")

elif usuario == "admin":
    if contrasena == "Admin#2024":
        print("ACCESO CONCEDIDO — admin: módulos de gestión habilitados.")
    else:
        print("DENEGADO — admin: contraseña incorrecta.")

elif usuario == "auditor":
    print("ACCESO LECTURA — auditor: modo consulta activado. Sesión registrada.")

elif usuario == "operador":
    if contrasena == "Oper@2024":
        print("ACCESO CONCEDIDO — operador: módulos operativos habilitados.")
    else:
        print("DENEGADO — operador: contraseña incorrecta.")

else:
    print(f"DENEGADO — usuario [{usuario}] no encontrado en el directorio.")