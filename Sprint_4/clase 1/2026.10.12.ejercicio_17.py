incidentes = ["txt-101",
              "txt-102",
              "txt-103",
              99,
              23.4,
              "txt-102"]

# tambien se puede incluir listas con diferentes tipos de datos
print("--- reporte de incidentes abiertos---listas con diferentes tipos de datos--")
# for ticket in incidentes:
#     #print("*",ticket)
#     print("*",ticket, type(ticket)) #para que nos arroje el tipo de dato que es cada elemento de la lista

# print("-----------------------------------")
# print("total: ",len(incidentes),"incidentes abiertos")

for k in range(len(incidentes)):
    print(k + 1, "-", incidentes[k]) #k+1 para que aparezca el numero de incidente y no el indice de la lista
