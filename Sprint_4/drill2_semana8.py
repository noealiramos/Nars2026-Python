# DRILL 2: LA CAJA FUERTE DE MATEO

# TODO 1: Crear la tupla con los tres valores.
config_escenario = (440, 8, 2000)

# TODO 2: Imprimir cada valor accediendo por índice.
print(f"Frecuencia base: {config_escenario[0]} Hz")
print(f"Canales: {config_escenario[1]}")
print(f"Potencia máxima: {config_escenario[2]} W")

# TODO 3: Descomenta esta línea para observar el error.
# Después, vuelve a comentarla para ejecutar sin errores.
# config_escenario[0] = 880

# TODO 4: Mostrar el tipo de dato.
print(type(config_escenario))