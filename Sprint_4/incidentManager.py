# GESTOR DE INCIDENTES — SonidoLibre
# Un sistema básico para registrar y resolver incidentes técnicos.

incidentes = []

# TODO 1: Agregar los 3 incidentes con append()
incidentes.append("microfono escenario principal sin señal")
incidentes.append("generador zona VIP con fluctuación")
incidentes.append("pantalla LED intermitente")

# TODO 2: Mostrar la lista completa y el número de incidentes
print("=== INCIDENTES REGISTRADOS ===")
print(incidentes)
print(f"Total de incidentes: {len(incidentes)}")

# TODO 3: Resolver el primer incidente y guardar el valor eliminado
incidente_resuelto = incidentes.pop(0)
print(f"\nSofía resolvió: {incidente_resuelto}")

# TODO 4: Agregar un incidente nuevo y mostrar la lista actualizada
incidentes.append("cable de poder roto en escenario 2")

print("\n=== LISTA ACTUALIZADA ===")
print(incidentes)

# TODO 5: Verificar si el incidente específico sigue abierto
print("\n=== BÚSQUEDA DE INCIDENTE ===")

if "generador zona VIP con fluctuación" in incidentes:
    print("El incidente del generador de la zona VIP sigue abierto.")
else:
    print("El incidente del generador de la zona VIP ya no está abierto.")

# TODO 6: Recorrer e imprimir todos los incidentes abiertos
print("\n=== INCIDENTES ABIERTOS ===")

for incidente in incidentes:
    print(f"→ {incidente}")