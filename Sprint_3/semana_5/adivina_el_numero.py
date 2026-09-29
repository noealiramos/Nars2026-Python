import random

# JUEGO: ADIVINA EL NÚMERO

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

while adivinado == False:
    intento = int(input("Adivina el número entre 1 y 10: "))
    intentos += 1

    if intento == numero_secreto:
        adivinado = True
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
    elif intento < numero_secreto:
        print("Muy bajo")
    else:
        print("Muy alto")

print("¡Gracias por jugar!")