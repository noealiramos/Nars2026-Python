# RETO AUTONOMO usando FOR y WHILE
# procesador_lotes.py

# Variables de entrada
lotes_pendientes = 5
transacciones_por_lote = 3
monto_por_transaccion = 1200.50
umbral_alerta = 10000

# Variables de control
lote_actual = 1
acumulado = 0
total_transacciones = 0
alerta_emitida = False

# Procesar los lotes
while lote_actual <= lotes_pendientes:

    # Procesar las transacciones de cada lote
    for transaccion in range(1, transacciones_por_lote + 1):

        acumulado = acumulado + monto_por_transaccion
        total_transacciones = total_transacciones + 1

        print(
            f"[Lote {lote_actual} | Trans {transaccion}] "
            f"Monto: ${monto_por_transaccion} | "
            f"Acumulado: ${acumulado:.2f}"
        )

        # Verificar si se cruzó el umbral
        if acumulado > umbral_alerta and alerta_emitida == False:
            print(
                f"[ALERTA] Umbral de ${umbral_alerta} excedido "
                f"en lote {lote_actual}, transacción {transaccion}"
            )
            alerta_emitida = True

    # Pasar al siguiente lote
    lote_actual = lote_actual + 1


# Resumen final
print(f"Total procesado: ${acumulado}")
print(f"Lotes procesados: {lotes_pendientes}")
print(f"Transacciones procesadas: {total_transacciones}")