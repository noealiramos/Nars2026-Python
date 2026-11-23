# ANTES: Código espagueti con variables globales
# nombre = "Inadaptado"
# nivel = 1
# experiencia = 0
#
# # Función que modifica globales (mal diseño)
# def subir_nivel():
#     global nivel, experiencia
#     experiencia = 0
#     nivel += 1
#     print(f"{nombre} subió al nivel {nivel}!")

# TU MISIÓN: refactoriza el código de arriba a funciones limpias con return.

print("=== SISTEMA DE NIVELES ===\n")


# TODO 1: Define crear_jugador(nombre_inicial) que devuelva un diccionario
# con las claves "nombre", "nivel" (empieza en 1) y "experiencia" (empieza en 0).
def crear_jugador(nombre_inicial):
    return {
        "nombre": nombre_inicial,
        "nivel": 1,
        "experiencia": 0,
    }


# TODO 2: Define ganar_experiencia(jugador, puntos): suma los puntos a
# jugador["experiencia"], imprime cuánto ganó y el total, y DEVUELVE el jugador.
def ganar_experiencia(jugador, puntos):
    jugador["experiencia"] += puntos
    print(f"{jugador['nombre']} ganó {puntos} XP. Total: {jugador['experiencia']} XP")
    return jugador


# TODO 3: Define subir_nivel(jugador): suma 1 al "nivel", reinicia
# "experiencia" a 0, imprime el nuevo nivel y DEVUELVE el jugador.
def subir_nivel(jugador):
    jugador["nivel"] += 1
    jugador["experiencia"] = 0
    print(f"¡{jugador['nombre']} subió al nivel {jugador['nivel']}!")
    return jugador


# TODO 4: Crea un jugador llamado "Inadaptado" con crear_jugador() e imprime
# su nombre y nivel inicial. Recuerda GUARDAR lo que devuelve la función.
jugador = crear_jugador("Inadaptado")
print(f"Jugador creado: {jugador['nombre']} (nivel {jugador['nivel']})\n")


# TODO 5: Haz que gane 50 XP y luego 100 XP llamando ganar_experiencia().
# En cada llamada reasigna: jugador = ganar_experiencia(jugador, ...)
jugador = ganar_experiencia(jugador, 50)
jugador = ganar_experiencia(jugador, 100)


# TODO 6: Si jugador["experiencia"] >= 100, llama subir_nivel() (reasignando).
if jugador["experiencia"] >= 100:
    jugador = subir_nivel(jugador)


# TODO 7: Haz que gane 75 XP más e imprime el estado final del diccionario.
jugador = ganar_experiencia(jugador, 75)
print(f"\nEstado final: {jugador}")