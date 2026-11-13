# DRILL 5: REPORTE DE ACREDITADOS — SOFÍA CIERRA LA SEMANA

# TODO 1: Reutiliza el archivero del drill anterior (3 diccionarios con
# claves "nombre" y "zona"). Cópialo aquí.
archivero = [
    {"nombre": "Ana López", "zona": "Carpa de prensa"},
    {"nombre": "Diego Ruiz", "zona": "Backstage"},
    {"nombre": "Mara Soto", "zona": "Zona VIP"},
]

# TODO 2: Imprime un encabezado para el reporte:
# "=== ACREDITACIONES SONIDOLIBRE 2026 ==="
print("=== ACREDITACIONES SONIDOLIBRE 2026 ===")

# TODO 3: Usa un for para iterar la lista. En cada vuelta, imprime una línea
# con el formato:
# "→ [nombre] | Zona: [zona]"
for acreditado in archivero:
    print(f"→ {acreditado['nombre']} | Zona: {acreditado['zona']}")

# TODO 4: Después del bucle (sin indentación), imprime el cierre con el total:
# "Total acreditados: [número]"
# (usa len() para el número)
print(f"Total acreditados: {len(archivero)}")