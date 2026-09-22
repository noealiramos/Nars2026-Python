# RETO AUTÓNOMO: clasificacion_riesgo.py (20 minutos de construcción)
# Estándar ISO 31000 — Gestión de Riesgos Empresariales.
# El sistema evalúa un proceso de negocio y lo clasifica según su nivel de riesgo.

# ── VARIABLES DE ENTRADA ────────────────────────────────────────────────
#   nombre_proceso  → str   (nombre del proceso evaluado)
#   probabilidad    → int   (1-5: probabilidad de que ocurra el riesgo)
#   impacto         → int   (1-5: magnitud del daño si ocurre)
#   con_controles   → str   ("si"/"no": ¿existen controles mitigantes vigentes?)

# ── CÁLCULOS REQUERIDOS (ANTES de los elif) ────────────────────────────
#   riesgo_inherente = probabilidad * impacto       (rango: 1-25)
#   Si con_controles == "si":
#       riesgo_residual = riesgo_inherente * 0.6    (reducción del 40%)
#   Si no:
#       riesgo_residual = riesgo_inherente

# ── CLASIFICACIÓN (más restrictivo PRIMERO) ────────────────────────────
#   riesgo_residual >= 20  →  CRÍTICO   · "Suspender proceso. Escalar a Dirección."
#   riesgo_residual >= 15  →  ALTO      · "Plan de mitigación en menos de 24 horas."
#   riesgo_residual >= 10  →  MEDIO     · "Revisión en próxima reunión de riesgos."
#   riesgo_residual >= 5   →  BAJO      · "Monitoreo periódico según calendario."
#   riesgo_residual < 5    →  MÍNIMO    · "Documentar y revisar en auditoría anual."

# ── FORMATO DE SALIDA ───────────────────────────────────────────────────
#   Debe incluir: nombre del proceso, riesgo inherente, riesgo residual y clasificación.
#   Ejemplo: "Proceso de pagos | Inherente: 20 | Residual: 12.0 → MEDIO"

nombre_proceso = input("nombre del proceso evaluado: ")
probabilidad = int(input("probabilidad de que ocurra el riesgo (1-5): "))
impacto = int(input("magnitud del daño si ocurre (1-5): "))
#con_controles = input("¿existen controles mitigantes vigentes? (si/no): ")
con_controles = input('"si"/"no": ¿existen controles vigetenes? ') #► mismo que el de arriba

riesgo_inherente = probabilidad * impacto
if con_controles == "si":
    riesgo_residual = riesgo_inherente * 0.6
else:
    riesgo_residual = riesgo_inherente
    
if riesgo_residual >= 20:
    clasificacion = "CRITICO"
    print(f"{clasificacion}")
elif  riesgo_residual >= 15:
    clasificacion = "ALTO"
    print(f"{clasificacion}")
elif  riesgo_residual >= 10:
    clasificacion = "MEDIO"
    print(f"{clasificacion}")
elif  riesgo_residual >= 5:
    clasificacion = "BAJO"
    print(f"{clasificacion}")
else:
    clasificacion = "MINIMO"
    print(f"{clasificacion}")
    
print(f"El {nombre_proceso} presenta riesgo inherente = {riesgo_inherente} | con riesgo residual = {riesgo_residual} | y su clasificacion es = {clasificacion=}")
# {clasificacion=} ►►► con el "=" al final, nos va a imprimir el nombre de LA VARIABLE CON SU VALOR

