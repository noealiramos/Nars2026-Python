# ENTREGABLE SPRINT 2: EL GUARDIÁN DE SONIDOLIBRE
print("=== SISTEMA DE ACCESO — SONIDOLIBRE 2026 ===")

# TODO 1: Credenciales fijas del sistema
usuario_correcto = "admin"
password_correcto = "sonido2026"

# TODO 2: Pedir usuario
usuario_ingresado = input("Ingresa tu usuario: ")

# TODO 3: Pedir contraseña
password_ingresado = input("Ingresa tu contraseña: ")

# TODO 4: Primer filtro - validar credenciales
if usuario_ingresado == usuario_correcto and password_ingresado == password_correcto:

    # Tercer filtro agregado: validar edad
    edad = int(input("Ingresa tu edad: "))

    if edad > 18:
        rol = input("Ingresa tu rol (admin/staff): ")

        # TODO 6: Segundo filtro - validar rol
        if rol == "admin":
            print("Acceso total concedido. Bienvenido al panel de control.")
        elif rol == "staff":
            print("Acceso estándar concedido. Bienvenido, staff de SonidoLibre.")
        else:
            print("Rol no reconocido. Acceso denegado.")

    else:
        print("Acceso denegado. Debes ser mayor de 18 años.")

# TODO 7: Credenciales incorrectas
else:
    if usuario_ingresado != usuario_correcto:
        print("Usuario no reconocido.")
    else:
        print("Contraseña incorrecta. Verifica tus datos.")
