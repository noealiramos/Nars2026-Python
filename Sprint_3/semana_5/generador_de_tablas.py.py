# GENERADOR DE TABLAS DE MULTIPLICAR

# TODO 1: Pedir el número
numero = int(input("¿De qué número quieres la tabla? "))

# TODO 2: Mostrar el encabezado
print(f"Tabla del {numero}:")

# TODO 3: Mostrar las multiplicaciones del 1 al 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")