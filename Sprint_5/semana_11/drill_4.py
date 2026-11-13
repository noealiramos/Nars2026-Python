# DRILL 4: EL GRAN ARCHIVERO DE OMAR

# TODO 1: Crea una lista vacía llamada 'archivero'.
archivero = []

# TODO 2: Usa .append() para agregar TRES diccionarios, uno por uno.
# Cada diccionario debe tener las claves "nombre" y "zona":
# - Ana López → Carpa de prensa
# - Diego Ruiz → Backstage
# - Mara Soto → Zona VIP
archivero.append({"nombre": "Ana López", "zona": "Carpa de prensa"})
archivero.append({"nombre": "Diego Ruiz", "zona": "Backstage"})
archivero.append({"nombre": "Mara Soto", "zona": "Zona VIP"})

# TODO 3: Imprime la lista completa para ver la estructura final.
print(archivero)

# TODO 4: Accede al nombre del SEGUNDO acreditado (Diego Ruiz)
# usando primero el índice de la lista y luego la clave del diccionario.
# Imprímelo con una f-string.
# Ejemplo:
# "Segundo acreditado: Diego Ruiz"
print(f"Segundo acreditado: {archivero[1]['nombre']}")