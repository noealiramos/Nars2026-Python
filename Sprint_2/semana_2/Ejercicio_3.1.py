# DETECTOR VIP — SonidoLibre
# El sistema de Regina para la Zona VIP del Parque Granado

# TODO 1: Pide la edad con input() y conviértela a int.
# Guárdala en una variable llamada 'edad'.
edad = int(input("¿Cuántos años tienes? "))

# TODO 2: Pide el dinero con input() y conviértelo a float.
# Guárdalo en una variable llamada 'dinero'.
dinero = float(input("¿Cuánto dinero tienes? "))

# TODO 3: Crea una variable llamada 'acceso_concedido'.
# Asígnale una expresión que verifique si edad >= 18 AND dinero >= 500.
acceso_concedido = edad >= 18 and dinero >= 500


# TODO 4: Usa print() con f-string para mostrar el resultado.
# Ejemplo de salida: "¿Puedes entrar a la Zona VIP?: True"
print(f"¿Puedes entrar a la Zona VIP?: {acceso_concedido}")