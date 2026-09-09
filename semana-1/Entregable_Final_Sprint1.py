# ENTREGABLE SPRINT 1: SISTEMA DE BIENVENIDA DE SONIDOLIBRE

print("=== BIENVENIDO A SONIDOLIBRE 2026 ===")

# TODO 1: Usa input() para pedir el nombre del asistente
# y guárdalo en una variable.
nombre = input("Ingresa tu nombre: ")

# TODO 2: Usa input() para pedir la ciudad de origen del asistente.
ciudad = input("Ingresa tu ciudad de origen: ")

# TODO 3: Usa input() con int() para pedir el año de nacimiento.
# Recuerda: int() convierte el texto que devuelve input() a número entero.
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# TODO 4: Calcula la edad restando el año de nacimiento al año actual (2026).
# Guarda el resultado en una variable llamada 'edad'.
edad = 2026 - anio_nacimiento

# TODO 5: Usa print() con f-strings para mostrar el resumen de bienvenida.
# Debe incluir el nombre, la ciudad y la edad calculada.
# Ejemplo de salida:
# "Bienvenido a SonidoLibre, [nombre] de [ciudad]. Tienes [edad] años.
# ¡Que disfrutes el festival!"
print(
    f"Bienvenido a SonidoLibre, {nombre} de {ciudad}. "
    f"Tienes {edad} años. ¡Que disfrutes el festival!"
)