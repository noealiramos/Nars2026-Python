# DRILL 1: LA LAVADORA DE STRINGS DE LUCÍA

# TODO 1: Crea una variable llamada 'nombre_sucio' con el siguiente texto
# (incluye los espacios y las mayúsculas raras tal cual están):
# "   dIaRiO DeL sUr   "
nombre_sucio = "   dIaRiO DeL sUr   "

# TODO 2: Aplica .strip() al string para quitarle los espacios.
# Guarda el resultado en una variable llamada 'sin_espacios'.
sin_espacios = nombre_sucio.strip()

# TODO 3: Aplica .lower() a 'sin_espacios' para volverlo todo minúsculas.
# Guarda el resultado en una variable llamada 'normalizado'.
normalizado = sin_espacios.lower()

# TODO 4: Aplica .title() para darle formato de título.
# Guarda el resultado en una variable llamada 'limpio'.
limpio = normalizado.title()

# TODO 5: Imprime las cuatro versiones para ver la transformación paso a paso.
# Pista: usa f-strings y comillas alrededor de cada uno para que se vean los espacios.
print(f"Original:     '{nombre_sucio}'")
print(f"Sin espacios: '{sin_espacios}'")
print(f"Normalizado:  '{normalizado}'")
print(f"Limpio:       '{limpio}'")