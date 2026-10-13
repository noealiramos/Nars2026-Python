incidentes = ["txt-101", 
              "txt-102", 
              "txt-103",
              "txt-104",
              "txt-102"]

if "txt-102" in incidentes:
    print("El incidente txt-102 está presente en la lista.")
    incidentes.remove("txt-102")
    print(incidentes)
else:
    print("El incidente txt-102 no está presente en la lista.")