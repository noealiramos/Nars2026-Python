# lab_listas.py — Sprint 4 · Clase 7
# Anatomía de una lista: leer, mutar y buscar sin reventar.

# ── Crear y leer ────────────────────────────────────────────────────────────
incidentes = [
    "TKT-101: red caída en piso 3",
    "TKT-102: impresora sin tóner",
    "TKT-103: usuario sin acceso a CRM",
    "TKT-104: solicitud de licencia de software",
]

print(incidentes[0])    # primer elemento
print(incidentes[-1])   # último elemento (índice negativo)
print(len(incidentes))  # cuántos hay
print("Índice máximo válido:", len(incidentes) - 1)

# Slicing: devuelve una NUEVA lista, no modifica la original.
print(incidentes[0:3])  # primeros 3
print(incidentes[-2:])  # últimos 2

# ── Mutar: métodos que cambian la lista en su lugar ──────────────────────────
incidentes.append("TKT-105: VPN intermitente")   # agrega al final
incidentes.insert(0, "TKT-URGENT: caída del ERP")  # inserta en posición 0

ultimo_cerrado = incidentes.pop()   # saca y DEVUELVE el último
print("Cerrado:", ultimo_cerrado)

# OJO: nunca hagas  incidentes = incidentes.append(...)  → .append() devuelve None.

# ── Buscar antes de borrar (evita ValueError) ────────────────────────────────
if "TKT-102: impresora sin tóner" in incidentes:
    incidentes.remove("TKT-102: impresora sin tóner")

# Evitar duplicados con not in.
nuevo = "TKT-200: monitor sin señal"
if nuevo not in incidentes:
    incidentes.append(nuevo)

# ── Reporte numerado para humanos (interno 0, externo 1) ─────────────────────
print("\n--- REPORTE DE INCIDENTES ABIERTOS ---")
for i in range(len(incidentes)):
    print(f"{i + 1}. {incidentes[i]}")
print("Total:", len(incidentes))
