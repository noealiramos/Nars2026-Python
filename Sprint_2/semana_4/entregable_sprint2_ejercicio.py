# # ENTREGABLE SPRINT 2: SISTEMA DE LOGIN
# usuario = input("Usuario: ")
# contrasena = input("Contraseña: ")

# # TODO 1: Escribe un if que verifique si usuario == "admin".
# # Dentro de ese bloque, agrega un if anidado para revisar la contraseña.
# if usuario == "admin":

# # TODO 2: Si contrasena == "1234", imprime:
# # "Acceso total concedido. Bienvenido, administrador."
#     if contrasena == "1234":
#         print("Acceso total concedido. Bienvenido, administrador.")
    
# # TODO 3: Si la contraseña del admin es incorrecta, imprime:
# # "Contraseña incorrecta. Acceso denegado."
#     else:
#         print("Contraseña incorrecta. Acceso denegado.")

# # TODO 4: Agrega un elif para usuario == "invitado".
# # El invitado no necesita contraseña.
# # Imprime: "Bienvenido, invitado. Tienes acceso limitado."
# elif usuario == "invitado":
#     print("Bienvenido, invitado. Tienes acceso limitado.")
# # TODO 5: Agrega un else final para cualquier otro usuario.
# # Imprime: "Usuario no encontrado. Acceso denegado."
# else:
#     print("Usuario no encontrado. Acceso denegado.")
    
    
# ENTREGABLE SPRINT 2: SISTEMA DE LOGIN
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso total concedido. Bienvenido, administrador.")
    else:
        print("Contraseña incorrecta. Acceso denegado.")

elif usuario == "invitado":
    print("Bienvenido, invitado. Tienes acceso limitado.")

else:
    print("Usuario no encontrado. Acceso denegado.")