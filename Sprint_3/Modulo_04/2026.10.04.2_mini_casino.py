import random

# MINI CASINO

# === JUEGO 1: Lanzar dos dados ===
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

print(f"Dado 1: {dado1}, dado 2: {dado2}, suma: {suma}")

if suma == 7:
    print("¡JACKPOT! Sacaste 7")
else:
    print("Sigue intentando")


# === JUEGO 2: Sorteo de premio ===

participantes = ["Noe", "Ana", "Luis", "María", "Carlos"]
ganador = random.choice(participantes)

print(f"El ganador es: {ganador}")


# === JUEGO 3: Lotería (5 números del 1 al 50) ===

numeros_loteria = []

for i in range(5):
    numero = random.randint(1, 50)
    numeros_loteria.append(numero)

print(f"Números de la lotería: {numeros_loteria}")


# === BONUS: Contraseña aleatoria de 6 caracteres ===

caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

for i in range(6):
    password += random.choice(caracteres)

print(f"Contraseña aleatoria: {password}")