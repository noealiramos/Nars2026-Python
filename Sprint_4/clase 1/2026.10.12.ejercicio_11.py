incidentes = ["txt-101: adfadfadf", 
              "txt-102: adadfadfad", 
              "txt-103: adfadafadff",
              "txt-104:adfadsfasdafd"]

# resultado = incidentes.append["txt-105: adfadsfasdf"]
# print("resultado de append: ", resultado)
# print("lista ", incidentes)

incidentes.insert(0,"txt-ticket urgente") #lo adiciona al inicio de la listaq
print(incidentes)

ticket_eliminado = incidentes.pop() #elimina el ultimo elemento de la lista
print("ticket eliminado: ", ticket_eliminado)
print("lista actualizada: ", incidentes)
print(f"{'-'* 20}") #--------------------
print(f"{ticket_eliminado} la lista actualizada quedo asi : {incidentes}")

print(f"{'-'* 20}") #--------------------
incidentes.pop(0) #elimina el primer elemento de la lista
print("lista actualizada: ", incidentes) 

# print(f"{'-'* 20}") #--------------------   
# incidentes.pop(99) # elimina el elemento de la posicion 99 de la lista, si no existe, genera un error
# print("lista actualizada: ", incidentes) 

