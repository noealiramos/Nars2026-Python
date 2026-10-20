
import math

# === LISTAS INICIALES ===

incidencias = [
    "caida del server",
    "fuga de datos",
    "ticket vencido",
    "backup fallido",
    "permisos"
]

prioridades = ["critica", "critica", "media", "alta", "baja"]
horas = [2, 12, 3, 6, 1]


# === MOSTRAR INCIDENTES CRITICOS ===

print("\n==== SOLO CRITICAS ====")

posicion = 0
total_incidentes_criticos = 0

for incidencia in incidencias:
    if prioridades[posicion] == "critica":
        print(f"[{posicion + 1}] {incidencia}")
        total_incidentes_criticos += 1

    posicion += 1


# === CALCULAR HORAS ===

total_horas = 0
total_criticas = 0
posicion = 0

for incidencia in incidencias:
    total_horas += horas[posicion]

    if prioridades[posicion] == "critica":
        total_criticas += horas[posicion]

    posicion += 1

print(f"\nHoras totales del backlog: {total_horas}")
print(f"Horas solo de criticas: {total_criticas}")
print(f"Total de incidentes criticos: {total_incidentes_criticos}")


# === ORDENAR INCIDENTES ALFABETICAMENTE ===

incidencias_ordenadas = sorted(incidencias)

numero = 1

print("\n==== INCIDENTES ORDENADOS ====")

for incid in incidencias_ordenadas:
    print(f"{numero}. {incid}")
    numero += 1


# === ORDENAR INCIDENTES POR HORAS ===

incidencias = [
    "caida del server",
    "fuga de datos",
    "ticket vencido",
    "backup fallido",
    "permiso de firma"
]

horas = [8, 12, 4, 6, 1]

# Combinar incidencias con sus horas
incidencias_horas = list(zip(incidencias, horas))

print("\n==== INCIDENCIAS CON HORAS ====")
print(incidencias_horas)

# Ordenar de mayor a menor por horas
incidencias_horas.sort(key=lambda x: x[1], reverse=True) #

print("\n==== INCIDENCIAS ORDENADAS POR HORAS ====")

for elemento in incidencias_horas:
    print(elemento)


# === CALCULAR DIAS HABILES MINIMOS ===

total_inc = len(incidencias)
por_dia = 4

dias_minimos = math.ceil(total_inc / por_dia)

print(f"\nIncidencias: {total_inc}")
print(f"Dias habiles minimos: {dias_minimos}")

print(f"floor({total_inc}/{por_dia}) = {math.floor(total_inc / por_dia)}")
print(f"ceil({total_inc}/{por_dia}) = {math.ceil(total_inc / por_dia)}")
