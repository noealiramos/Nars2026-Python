#varios tipos de datos en el dicccionario
jugador = {'nombre':'link','juego':'leyend of zelda','puntos':42,'activo':True}

#ya no se usan indices numericos (como en la lista)
print(jugador['nombre'])
print(jugador['juego'])

print("====claves disponibles=========")

#para obtener las claves disponibles del diccionario
for clave in jugador.keys():
    print(clave)

print("====valores disponibles=========")
for valor in jugador.values():
    print(valor)

print("====items disponibles=========")
for clave,valor in jugador.items():
    print(f"{clave}: {valor}")
    
jugadores = [
    {"nombre":"link","juego":"zelda","nivel":42},
    {"nombre":"samus","juego":"metroid","nivel":87},
    {"nombre":"kirby","juego":"kirby","nivel":15},
]

print(jugadores)