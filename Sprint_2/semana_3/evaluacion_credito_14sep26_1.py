#── VARIABLES DE ENTRADA ───────────────────────────────────────────────────
#   nombre                 → str   (nombre completo del solicitante)
#   ingreso_mensual  → float (ingreso neto mensual en pesos)
#   deuda_mensual    → float (total de pagos de deuda actuales por mes)
#   tipo_empleo          → str   ("permanente" / "contrato" / "independiente" / "desempleado")
#   score_crediticio     → int   (score de buró, rango 300-850)
#   antiguedad_años  → int   (años en el empleo actual o en actividad independiente)
  
# ── REGLAS DE NEGOCIO (en este orden exacto) ────────────────────────────────
#   Regla 1: tipo_empleo == "desempleado"
#            → DENEGADO: sin actividad económica activa

#   Regla 2: score_crediticio < 500
#            → DENEGADO: score en rango de alto riesgo

#   Regla 3: ratio_deuda > 0.50
#            → DENEGADO: más del 50% del ingreso comprometido en deudas

#   Regla 4: tipo_empleo == "independiente" AND antiguedad_años < 3
#            → DENEGADO: actividad independiente con menos de 3 años de antigüedad

#   Regla 5: score_crediticio >= 750 AND ratio_deuda <= 0.25 AND tipo_empleo == "permanente"
#            → APROBADO: tasa preferencial (el mejor perfil)

#   Regla 6: score_crediticio >= 600 AND ratio_deuda <= 0.40
#            → APROBADO: tasa estándar

#   Regla 7: score_crediticio >= 500 AND ratio_deuda <= 0.50
#            → PENDIENTE: requiere análisis adicional por un ejecutivo

#   Regla 8 (else): Ninguna condición anterior fue True
#            → DENEGADO: perfil no cumple ningún criterio de aprobación


#►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►
# Inputs del caso
# Resultado esperado
# ¿Qué detecta?
# 1
# Permanente · $45,000 ingreso · $9,000 deuda (ratio 20%) · score 790 · 8 años
# APROBADO preferencial
# Caso ideal: ¿llega a la Regla 5?
# 2
# Independiente · $30,000 · $6,000 (ratio 20%) · score 710 · 1.5 años
# DENEGADO (antigüedad insuficiente)
# ¿Regla 4 con AND correcto?
# 3
# Contrato · $20,000 · $11,000 (ratio 55%) · score 720 · 4 años
# DENEGADO (ratio excede 50%)
# ¿Regla 3 antes de Regla 6?
# 4
# Desempleado · $0 · $0 · score 680 · 0 años
# DENEGADO (sin actividad económica)
# ¿División por cero? Regla 1 debe atrapar esto antes del cálculo
# 5
# Permanente · $50,000 · $18,000 (ratio 36%) · score 640 · 12 años
# APROBADO estándar
# ¿Regla 6 con ratio <= 0.40?
# 6
# Permanente · $60,000 · $24,000 (ratio 40%) · score 520 · 7 años
# PENDIENTE
# ¿Regla 7 cuando score es bajo pero ratio es limite exacto?
# 7
# Permanente · $35,000 · $8,750 (ratio 25%) · score 760 · 5 años
# APROBADO preferencial
# Ratio en el límite exacto de 25%. ¿<= o < en la condición?

#►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►►

  
#VARIABLES DE ENTRADA
nombre = input("Ingrese su nombre completo: ")
ingreso_mensual = float(input("Ingrese su ingreso neto mensual en pesos: "))
deuda_mensual = float(input("Ingrese el total de pagos de deuda actuales por mes: "))
tipo_empleo = input("Ingrese su tipo de empleo (permanente / contrato / independiente / desempleado): ")
score_crediticio = int(input("Ingrese su score de buró (rango 300-850): "))
antiguedad_años = float(input("Ingrese los años en el empleo actual o en actividad independiente: "))

#CALCULOS
ratio_deuda = deuda_mensual / ingreso_mensual
#    (Ejemplo: si ingreso=30,000 y deuda=9,000 → ratio = 0.30 = 30%)

capacidad_pago = ingreso_mensual - deuda_mensual
#  (Cuánto le queda disponible después de pagar deudas actuales)

  
#REGLAS DE NEGOCIO
if tipo_empleo == "desempleado":
    pre_evaluacion = "DENEGADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion} debido a que se encuentra desempleado.")

elif score_crediticio < 500:
    pre_evaluacion = "DENEGADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion} debido a que su score crediticio es menor a 500.")

elif ratio_deuda > 0.50:
    pre_evaluacion = "DENEGADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion} debido a que su ratio de deuda es mayor al 50%.")

elif tipo_empleo == "independiente" and antiguedad_años < 3:
    pre_evaluacion = "DENEGADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion} debido a que es independiente y tiene menos de 3 años de antigüedad.")

elif score_crediticio >= 750 and ratio_deuda <= 0.25 and tipo_empleo == "permanente":
    pre_evaluacion = "APROBADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion}. Felicidades, cumple con los requisitos para el crédito.")

elif score_crediticio >= 600 and ratio_deuda <= 0.40:  # REGLA 6
    pre_evaluacion = "APROBADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion}. Felicidades, cumple con los requisitos para el crédito.")

elif score_crediticio >= 500 and ratio_deuda <= 0.50:  # REGLA 7
    pre_evaluacion = "PENDIENTE"
    print(f"Estimado {nombre}, su solicitud de crédito está {pre_evaluacion}. Se requiere análisis adicional por un ejecutivo.")

else: #REGLA 8
    pre_evaluacion = "DENEGADO"
    print(f"Estimado {nombre}, su solicitud de crédito ha sido {pre_evaluacion}. No cumple con los criterios de aprobación.")    
    
    
    
    
    