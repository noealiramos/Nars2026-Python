# BUSCADOR DE NÚMEROS PARES
# TODO 1: Crea una variable 'numeros' con esta lista exacta:
# [1, 3, 5, 7, 8, 11, 13, 16, 19]


# === PARTE 1: Encontrar el primer par usando break ===
# TODO 2: Imprime "Buscando el primer número par..." antes del bucle.

# TODO 3: Recorre la lista 'numeros' con un for.
# Dentro del bucle imprime "Revisando [num]..." en cada vuelta.
# Si el número es par (pista: usa el operador módulo %, un número es par
# cuando 'num % 2 == 0'), imprime "¡Encontrado! El primer par es [num]"
# y usa break para salir del bucle.


# === PARTE 2: Imprimir solo los impares usando continue ===
# TODO 4: Imprime un encabezado: "Números impares de la lista:".

# TODO 5: Recorre otra vez la lista 'numeros' con un for.
# Si el número es par, usa continue para saltar esa vuelta.
# Si no, imprímelo. La salida final debe ser únicamente los impares
# en el mismo orden que aparecen en la lista.

#=========================SOLUCION==================================================


numeros = [1, 3, 5, 7, 8, 11, 13, 16, 19]

print("Buscando el primer número par...")

for num in numeros:
    print(f"Revisando {num}...")
    if num % 2 == 0:
        print(f"¡Encontrado! El primer par es {num}")
        break

print("Números impares de la lista:")
for num in numeros:
    if num % 2 == 0:
        continue
    
    print(num)
