# ritual_clase7.py — Sprint 4 · Clase 7
# La trampa del slicing y el índice fantasma.
# Predice qué imprime cada línea ANTES de ejecutar.

tickets = ["TKT-101", "TKT-102", "TKT-103", "TKT-104"]

print(len(tickets[1:3]))   # 2  → slicing semi-abierto: índices 1 y 2 (el 3 NO entra)
print(tickets[-2])         # TKT-103 → índice negativo: el penúltimo
print(tickets[3])          # TKT-104 → último índice válido = len(lista) - 1

# La línea de abajo REVIENTA a propósito: el índice 4 no existe en una lista
# de 4 elementos (índices válidos 0..3). Descoméntala para ver el IndexError.
# print(tickets[4])        # IndexError: list index out of range
