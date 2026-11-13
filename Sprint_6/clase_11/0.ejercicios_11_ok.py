#salario valida entre 8000 y 200000, inclusive ambos. cualquier cosa fuera de ese rango es suspechoso

def es_salario_valildo(salario):
    return 8000 <= salario <= 200000

print(es_salario_valildo(9000))  # True

""" #doc string debajo del text de lo que se quiere explicar
    esta funcion sirve para validar si un salario es valido o no. Un salario es valido si esta entre 8000 y 200000, inclusive ambos. Cualquier cosa fuera de ese rango es sospechoso.
"""