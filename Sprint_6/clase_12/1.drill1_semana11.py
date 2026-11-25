# DRILL 1: LA MÁQUINA CONVERSORA DE XIMENA

# TODO 1: Define una función llamada 'metros_a_pies' que reciba un parámetro
# llamado 'metros'. Dentro de la función, usa return para devolver
# el resultado de multiplicar metros por 3.28084.
def metros_a_pies(metros):
    return metros * 3.28084


# TODO 2: Llama a la función con el valor 10 y guarda el resultado
# en una variable llamada 'distancia_pies'.
distancia_pies = metros_a_pies(10)


# TODO 3: Imprime el resultado con una f-string.
# Ejemplo:
# "10 metros equivalen a 32.8084 pies"
print(f"10 metros equivalen a {distancia_pies} pies")


# TODO 4: Llama la función dos veces más con valores distintos
# (por ejemplo 5 y 25) e imprime ambos resultados.
distancia_5 = metros_a_pies(5)
print(f"5 metros equivalen a {distancia_5} pies")

distancia_25 = metros_a_pies(25)
print(f"25 metros equivalen a {distancia_25} pies")