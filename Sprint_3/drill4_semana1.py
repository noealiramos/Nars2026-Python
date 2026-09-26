import random

# DRILL 4: EL MINI-JUEGO DE LUCÍA

secreto = random.randint(1, 10)
intento = int(input("Adivina el número entre 1 y 10: "))

while intento != secreto:
    intento = int(input("No es ese. Intenta de nuevo: "))

print(f"¡Acertaste! El número era {secreto}.")