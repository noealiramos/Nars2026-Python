# DRILL 3: LA VALIDACIÓN DE CREDENCIALES DE REGINA

# TODO 1: Define una función llamada 'tiene_acceso_backstage' que reciba
# un parámetro llamado 'tipo_credencial' (será un string).
# La función debe devolver True si el tipo es "staff" o "artista".
# En cualquier otro caso, debe devolver False.
def tiene_acceso_backstage(tipo_credencial):
    # Revisamos si la credencial está en la lista de tipos permitidos.
    # "in" devuelve True si el valor está en la lista y False si no está.
    return tipo_credencial in ["staff", "artista"]


# TODO 2: Llama la función con "artista" e imprime el resultado.
print(tiene_acceso_backstage("artista"))   # Imprime: True


# TODO 3: Llama la función con "prensa" e imprime el resultado.
print(tiene_acceso_backstage("prensa"))    # Imprime: False


# TODO 4: Usa la función dentro de un if para imprimir un mensaje legible.
tipo = "staff"

# Como la función ya devuelve True o False, la usamos directo como condición del if.
if tiene_acceso_backstage(tipo):
    print("Acceso permitido a backstage")
else:
    print("Acceso denegado")
