#salario valida entre 8000 y 200000, inclusive ambos. cualquier cosa fuera de ese rango es suspechoso
tasa_impuesto = 0.10

def usar_tasa_promo():
    tasa_impuesto=0.05
    return tasa_impuesto

promo = usar_tasa_promo()
print(f"tasa promo devuelte: {promo}")
print(f"tasa global del sitema: {tasa_impuesto}")