incidencias_ordenadas = sorted(incidencias)

print("\n=== ORDEN DE CAPTURA (original, intacto) ===")
numero = 1
for inc in incidencias:
    print(f"{numero}. {inc}")
    numero = numero + 1

print("\n=== VISTA ALFABÉTICA (para dirección) ===")
numero = 1
for inc in incidencias_ordenadas:
    print(f"{numero}. {inc}")
    numero = numero + 1