#NOTA► while: se detiene cuando se cumple una condición
# tickets_restantes = 100
# while tickets_restantes > 0:
#     print(f"Se vendió el ticket: {tickets_restantes}")
#     tickets_restantes -= 1


#================================

#NOTA► for: da exactamente 50 vueltas
# for i in range(50): #el for llegará a 49, ya que empieza en 0
#     print(f"Imprimiendo copia {i + 1}")
    

#================================
    
# NOTA► range(1, 5) genera: 1, 2, 3, 4  (NO genera el 5)
# for i in range(1, 5): #el range 5 llegará a 4
#     print(i)

# COMENTARIO► range(N) es equivalente a range(0, N)
# COMENTARIO► genera: 0, 1, 2, ..., N-1

#================================


lotes = 3
elementos = 4

while lotes > 0:
    print(f"Lote en proceso. Quedan {lotes}.")
    for i in range(elementos):
        print(f"  Elemento {i + 1}/{elementos}")
    lotes -= 1  # si olvidas esta línea, el while es infinito