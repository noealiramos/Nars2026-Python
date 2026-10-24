# DRILL 3: LAS MESAS DE VALENTINA

# TODO 1: Importar el módulo math
import math

# TODO 2: Definir las variables
asistentes_vip = 487
capacidad_mesa = 8
kilos_carne = 120
peso_porcion = 0.25

# TODO 3: Calcular las mesas necesarias, redondeando hacia arriba
mesas_necesarias = math.ceil(asistentes_vip / capacidad_mesa)

# TODO 4: Calcular las porciones completas, redondeando hacia abajo
porciones_servibles = math.floor(kilos_carne / peso_porcion)

# TODO 5: Imprimir los resultados con f-strings
print(f"Mesas a comprar: {mesas_necesarias}")
print(f"Porciones servibles: {porciones_servibles}")