# CALIBRACIÓN — observa cómo se comporta random

# TODO 1: Importa el módulo random.
import random

# TODO 2: Genera e imprime un entero aleatorio entre 1 y 20.
numero = random.randint(1, 20)
print(numero)

# TODO 3: Elige e imprime un emoji.
emojis = ["🐶", "🐱", "🐰", "🦊"]
emoji = random.choice(emojis)
print(emoji)

# TODO 4: Mezcla los días e imprime la lista después.
dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
random.shuffle(dias)
print(dias)