lotes_pendientes = 3
elementos_por_lote = 4
lote_actual = 1
total_tickets = 0

while lotes_pendientes > 0:
    print(f"=== Procesando lote {lote_actual} de {lote_actual + lotes_pendientes - 1} ===")
    for i in range(elementos_por_lote):
        print(f"  Ticket {i + 1}/{elementos_por_lote} procesado")
        total_tickets += 1
    lotes_pendientes -= 1
    lote_actual += 1

print(f"Todos los lotes procesados. Total de tickets: {total_tickets}")