# Sistema de Ficha de Recluta

print("=== REGISTRO DE RECLUTA ===\n")


# TODO 1: Crea el diccionario 'recluta' con al menos 5 claves:
#   "nombre", "edad", "rango", "puntos" y "especialidad".
recluta = {
    "nombre": "Ana",
    "edad": 24,
    "rango": "Novato",
    "puntos": 350,
    "especialidad": "Python",
}


# TODO 2: Imprime "--- FICHA COMPLETA ---" y recorre el diccionario
# con un bucle 'for clave, valor in recluta.items():' mostrando
# cada par como "Clave: valor".
print("--- FICHA COMPLETA ---")
for clave, valor in recluta.items():
    print(f"{clave.capitalize()}: {valor}")


# TODO 3: Imprime "--- PROMOCIÓN ---". Cambia el "rango" a "Aprendiz"
# y suma 150 a los "puntos". Imprime el nuevo rango y los puntos totales.
print("\n--- PROMOCIÓN ---")
recluta["rango"] = "Aprendiz"
recluta["puntos"] += 150
print(f"Nuevo rango: {recluta['rango']}")
print(f"Puntos totales: {recluta['puntos']}")


# TODO 4: Agrega dos claves nuevas al diccionario:
#   "proyecto_actual" (un string) y "mentores" (una lista de nombres).
recluta["proyecto_actual"] = "Sistema de inventario"
recluta["mentores"] = ["Carlos", "Lucía"]


# TODO 5: Imprime "--- CAMPOS DISPONIBLES ---" y recorre solo las claves
# con recluta.keys(), imprimiendo cada una con un prefijo "- ".
print("\n--- CAMPOS DISPONIBLES ---")
for clave in recluta.keys():
    print(f"- {clave}")


# TODO 6: Usa .get("certificaciones", []) para leer un campo que puede
# no existir SIN provocar un KeyError. Imprime el resultado.
certificaciones = recluta.get("certificaciones", [])
print(f"\nCertificaciones: {certificaciones}")


# TODO 7: Usa 'if "proyecto_actual" in recluta:' para verificar que existe
# y elimínalo con .pop(), guardando el valor devuelto. Imprime qué eliminaste.
if "proyecto_actual" in recluta:
    eliminado = recluta.pop("proyecto_actual")
    print(f"Proyecto eliminado: {eliminado}")


# TODO 8: Imprime "--- FICHA FINAL ---" y vuelve a recorrer el diccionario
# con .items() para mostrar cómo quedó la ficha.
print("\n--- FICHA FINAL ---")
for clave, valor in recluta.items():
    print(f"{clave.capitalize()}: {valor}")
