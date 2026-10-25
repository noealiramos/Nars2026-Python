prioridades = ["critica", "critica", "media", "alta", "baja"]

print("\n=== SOLO CRÍTICAS ===")
posicion = 0
for incidencia in prioridades:
    if prioridades[posicion] == "critica":
        print(f"[!] {incidencia}")
    posicion = posicion + 1