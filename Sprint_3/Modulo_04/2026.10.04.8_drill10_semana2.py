# DRILL 10: EL CONTEO SELECTIVO DE CHECO

contador_aforo = 0

for credencial in range(1, 21):
    if credencial % 5 == 0:
        continue

    contador_aforo += 1
    print(f"Credencial {credencial} contada -- aforo actual {contador_aforo}")

print(f"Aforo oficial del día: {contador_aforo} personas (cortesías excluidas).")