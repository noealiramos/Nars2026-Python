incidentes = ["txt-101", 
              "txt-102", 
              "txt-103",
              99,
              23.4,
              "txt-102"]

print("--- reporte de incidentes abiertos---listas con diferentes tipos de datos--") #tambien se puede incluir listas con diferentes tipos de datos, pero no es recomendable
for ticket in incidentes:
    #print("*",ticket)
    print("*",ticket, type(ticket)) #para que nos arroje el tipo de dato que es cada elemento de la lista
    
print("-----------------------------------")
print("total: ",len(incidentes),"incidentes abiertos")