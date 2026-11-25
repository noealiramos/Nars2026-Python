# DRILL 5: REFACTORIZANDO EL ESPAGUETI DE SOFÍA

# TODO 1: Definimos la función UNA sola vez
def pedir_dato_limpio(etiqueta):
    # 'etiqueta' es el parámetro: el texto que verá el usuario.
    # Cambia en cada llamada, por eso no se escribe "fijo" dentro de la función.
    dato = input(etiqueta)

    # .strip() quita los espacios sobrantes al inicio y al final: "  bad bunny  " -> "bad bunny"
    # .title() pone en mayúscula la primera letra de cada palabra: "bad bunny" -> "Bad Bunny"
    # Se pueden encadenar porque cada método devuelve un string nuevo.
    dato_limpio = dato.strip().title()

    # return ENTREGA el resultado a quien llamó la función.
    # Sin return, la función devolvería None y perderías el dato.
    return dato_limpio


# TODO 2: Usamos (llamamos) la función tres veces
# Cada llamada manda una etiqueta distinta y guarda lo que devuelve en su propia variable.
artista = pedir_dato_limpio("Nombre del artista: ")
medio = pedir_dato_limpio("Nombre del medio de prensa: ")
zona = pedir_dato_limpio("Zona asignada: ")


# TODO 3: Imprimimos con f-strings
# La f antes de las comillas permite meter variables dentro de {llaves}.
print(f"Artista: {artista}")
print(f"Medio de prensa: {medio}")
print(f"Zona asignada: {zona}")


# TODO 4 (reflexión):
# Sin función, el bloque input + strip + title (unas 2-3 líneas) se repetiría 3 veces: ~9 líneas.
# Con función: 4 líneas de definición + 3 llamadas = 7 líneas.
# En este caso ahorras pocas líneas, y eso no es lo importante. Lo que ganas es que
# si mañana quieres cambiar la limpieza (por ejemplo, usar .upper() en lugar de .title()),
# lo cambias en UN solo lugar y no en tres. Eso es refactorizar: el resultado es el mismo
# y el código queda más fácil de mantener.