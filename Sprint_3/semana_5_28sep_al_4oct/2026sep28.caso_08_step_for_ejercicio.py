brinco=0

#pagos quincenales del año cada 15 dias, suponiendo 360 dias al año
print("\n fechas de pago quincenales")
for dia_del_anio in range(15,361,15): # step► desde el dia 15 (dato izq) , va a saltar cada 15 dias (dato de la derecha)
    brinco= brinco+1
    print(f"pago programado: dia {dia_del_anio} y brinco: {brinco}")