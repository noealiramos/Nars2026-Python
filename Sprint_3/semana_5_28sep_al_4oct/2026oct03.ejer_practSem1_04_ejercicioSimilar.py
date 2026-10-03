# PROCESADOR DE LOTES — SonidoLibre

lotes_pendientes = 3
elementos_por_lote = 4
lote_actual = 1

lotes_pendientes_original = lotes_pendientes

# TODO 1: Continúa mientras haya lotes pendientes.
while lotes_pendientes > 0:

    # TODO 2: Imprime el inicio de cada lote.
    print(f"=== Procesando lote {lote_actual} de {lotes_pendientes_original} ===")

    # TODO 3: Procesa cada elemento del lote.
    for ticket in range(1, elementos_por_lote + 1):
        print(f"  Ticket {ticket}/{elementos_por_lote} procesado")

    # TODO 4: Actualiza los contadores.
    lotes_pendientes -= 1
    lote_actual += 1

# TODO 5: Imprime el total fuera de los bucles.
total = lotes_pendientes_original * elementos_por_lote
print(f"Todos los lotes procesados. Total de tickets: {total}")






lotes_pendientes = 3
elementos_por_lote = 4
lote_actual = 1

lotes_pendientes_original = lotes_pendientes

while lotes_pendientes > 0:
    print(f"=== Procesando lote {lote_actual} de {lotes_pendientes_original} ===")
    for ticket in range(1, elementos_por_lote + 1):
        print(f"  Ticket {ticket}/{elementos_por_lote} procesado")

    lotes_pendientes -= 1
    lote_actual += 1

total = lotes_pendientes_original * elementos_por_lote
print(f"Todos los lotes procesados. Total de tickets: {total}")