# DRILL 2: PASES EXTRA — OMAR ACTUALIZA EL EXPEDIENTE

# TODO 1: Diccionario con dos claves
periodista = {
    "nombre": "Ana López",
    "pases_extra": 0
}

# TODO 2: Sumar 1 con +=
periodista["pases_extra"] += 1

# TODO 3: Sumar otro pase (quedan 2)
periodista["pases_extra"] += 1

# TODO 4: Crear una clave nueva
periodista["fotografo_confirmado"] = True

# TODO 5: Resumen con f-string
print(f"{periodista['nombre']} tiene {periodista['pases_extra']} pases extra. Fotógrafo confirmado: {periodista['fotografo_confirmado']}")