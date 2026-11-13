# pago_bruto = sueldo_base + bono

# hay 4 empleados con sueldos y bonos distintos. Mañana habrá 40.
# no queremos escribir la suma 40 veces, queremos una maquina que dando el sueldo y bono, devuelva el bruto


def calcular_pago_bruto(sueldo_base, bono):
    bruto = sueldo_base + bono
    return bruto

pago = calcular_pago_bruto(20000, 2000)
print(f"el pago a depositar es: ${pago:.2f}")