# DRILL 5: EL REPORTE COMPLETO DE SOFÍA

# TODO 1: Mismo diccionario del drill anterior
acreditaciones = {
    "Ana López": "Carpa de prensa",
    "Diego Ruiz": "Backstage",
    "Mara Soto": "Zona VIP"
}

# TODO 2: Recorrer con .items()
for nombre, zona in acreditaciones.items():
    print(f"{nombre} → {zona}")

# TODO 3: Línea de cierre, fuera del bucle
print("Reporte generado correctamente.")