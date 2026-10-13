incidentes = ["txt-101", 
              "txt-102", 
              "txt-103",
              "txt-104",
              "txt-102"]

nuevo = "txt-105"

if nuevo not in incidentes:
    incidentes.append(nuevo)
    print(f"El incidente {nuevo} ha sido agregado a la lista.")
else:
    print(f"El incidente {nuevo} ya está presente en la lista.")
    
print(incidentes)
    