# ✅ Diseño limpio (sin globales)
IMPUESTO_IVA = 0.16  # Constante global (en mayúsculas por convención)

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_impuesto(subtotal):
    return subtotal * IMPUESTO_IVA

def calcular_total(precio, cantidad):
    subtotal = calcular_subtotal(precio, cantidad)
    impuesto = calcular_impuesto(subtotal)
    return subtotal + impuesto

# Uso
total = calcular_total(100, 3)
print(f"Total a pagar: {total:.2f} USD")  # Total a pagar: 348.00 USD