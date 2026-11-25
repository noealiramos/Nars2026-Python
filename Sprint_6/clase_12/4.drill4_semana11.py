# DRILL 4: EL ESPEJISMO DEL SCOPE

# TODO 1: Crea una variable global llamada 'asistentes_totales' con valor 400.
asistentes_totales = 400


# TODO 2: Define una función llamada 'agregar_asistentes' SIN parámetros.
# Dentro de la función:
#   - Crea una variable local también llamada 'asistentes_totales' con valor 50.
#   - Imprime esa variable local con un f-string que diga:
#     "Dentro de la función: [valor]"
def agregar_asistentes():
    asistentes_totales = 50
    print(f"Dentro de la función: {asistentes_totales}")


# TODO 3: Llama a la función.
agregar_asistentes()


# TODO 4: Después de la llamada, imprime la variable global con un f-string que diga:
# "Fuera de la función: [valor]"
print(f"Fuera de la función: {asistentes_totales}")

# Observa: los dos prints muestran números distintos. ¿Por qué?
# Respuesta: al asignar 'asistentes_totales = 50' dentro de la función, Python crea
# una variable LOCAL nueva que solo existe mientras la función se ejecuta. Esa
# variable "tapa" a la global dentro de la función, pero no la modifica. Al salir
# de la función, la local desaparece y la global sigue valiendo 400.