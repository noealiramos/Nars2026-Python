# CALCULADORA CON FUNCIONES

# TODO 1: Importar el módulo math.
import math


# ===== DEFINICIÓN DE FUNCIONES =====

# TODO 2: Mostrar bienvenida.
def mostrar_bienvenida():
    print("Bienvenido a la calculadora")
    print("Versión 1.0")


# TODO 3: Devolver la suma.
def sumar(a, b):
    return a + b


# TODO 4: Devolver la resta.
def restar(a, b):
    return a - b


# TODO 5: Dividir validando que el divisor no sea cero.
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"

    return a / b


# TODO 6: Calcular las cajas necesarias redondeando hacia arriba.
def calcular_cajas(productos, capacidad):
    return math.ceil(productos / capacidad)


# ===== USAR LAS FUNCIONES =====

# TODO 7: Imprimir el encabezado.
mostrar_bienvenida()

# TODO 8: Mostrar operaciones básicas.
print("\n=== Operaciones Básicas ===")
print(f"Suma de 10 + 5: {sumar(10, 5)}")
print(f"Resta de 10 - 5: {restar(10, 5)}")
print(f"División de 10 / 3: {dividir(10, 3)}")
print(f"División de 10 / 0: {dividir(10, 0)}")

# TODO 9: Mostrar redondeo y truncamiento.
print("\n=== Redondeo con math ===")
numero = 4.7

print(f"Valor original: {numero}")
print(f"Redondeo hacia arriba: {math.ceil(numero)}")
print(f"Redondeo hacia abajo: {math.floor(numero)}")
print(f"Truncamiento con int: {int(numero)}")

# TODO 10: Calcular y mostrar las cajas necesarias.
print("\n=== Cálculo de Cajas ===")
productos = 47
capacidad_caja = 10

cajas = calcular_cajas(productos, capacidad_caja)

print(f"Productos: {productos}")
print(f"Capacidad por caja: {capacidad_caja}")
print(f"Cajas necesarias: {cajas}")