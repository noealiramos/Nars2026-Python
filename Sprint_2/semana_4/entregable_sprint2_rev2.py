# ENTREGABLE SPRINT 2: EL GUARDIÁN DE SONIDOLIBRE

print("=== SISTEMA DE ACCESO — SONIDOLIBRE 2026 ===")

# TODO 1: Credenciales fijas del sistema
usuario_correcto = "admin"
password_correcto = "sonido2026"

# TODO 2: Pedir usuario
usuario_ingresado = input("Ingresa tu usuario: ")

# TODO 3: Pedir contraseña
password_ingresado = input("Ingresa tu contraseña: ")

# TODO 4: Verificar usuario y contraseña
if usuario_ingresado == usuario_correcto and password_ingresado == password_correcto:

    # TODO 5: Pedir rol
    rol = input("Ingresa tu rol (admin/staff): ")

    # TODO 6: Verificar rol
    if rol == "admin":
        print("Acceso total concedido. Bienvenido al panel de control.")
    else:
        print("Acceso estándar concedido. Bienvenido, staff de SonidoLibre.")

# TODO 7: Distinguir error de usuario o contraseña
else:
    if usuario_ingresado != usuario_correcto:
        print("Usuario no reconocido.")
    else:
        print("Contraseña incorrecta. Verifica tus datos.")