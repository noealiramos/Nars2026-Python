# DRILL 8: EL ACUMULADOR DE CHECO

total_asistentes = 0

for hora in range(1, 6):
    total_asistentes += hora
    print(f"Hora {hora}: total acumulado {total_asistentes}")

print(f"Total de asistentes del día: {total_asistentes} mil asistentes")