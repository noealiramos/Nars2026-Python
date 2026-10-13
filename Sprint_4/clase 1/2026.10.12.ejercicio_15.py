incidentes = ["txt-101", 
              "txt-102", 
              "txt-103",
              "txt-104",
              "txt-102"]

print("--- reporte de incidentes abiertos---")
for ticket in incidentes:
    print("*",ticket)
print("-----------------------------------")
print("total: ",len(incidentes),"incidentes abiertos")