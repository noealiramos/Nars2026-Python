# DRILL 3: LA CANCELACIÓN DE ÚLTIMO MINUTO

bandas_confirmadas = [
    "Los Granados",
    "Cardumen",
    "La Sierra",
    "Voltio Norte",
    "Mareas Altas"
]

# TODO 1: Elimina "Voltio Norte".
bandas_confirmadas.remove("Voltio Norte")

# TODO 2: Agrega "Espuma Fría" en el índice 3.
bandas_confirmadas.insert(3, "Espuma Fría")

# TODO 3: Imprime la lista actualizada.
print(bandas_confirmadas)

# TODO 4: Retira la última banda y guarda el resultado.
banda_retirada = bandas_confirmadas.pop()

# TODO 5: Imprime el mensaje y la lista final.
print(f"Banda retirada del cartel: {banda_retirada}")
print(bandas_confirmadas)