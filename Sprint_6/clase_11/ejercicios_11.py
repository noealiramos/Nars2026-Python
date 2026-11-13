tasa_impuesto = 0.10 #variable global

def calcular_pago_bruti(sueldo_base, bono):
    total = sueldo_base + bono
    return total

pago = calcular_pago_bruti(2000, 2000)
print(f"el pago a depositar es: {pago}")

def recalcular_tasa():
    tasa_impuesto= 0.12 # variable interna
    return tasa_impuesto

recalcular_tasa()
print(f"tasa vigente del sistema {tasa_impuesto:.2f}")
