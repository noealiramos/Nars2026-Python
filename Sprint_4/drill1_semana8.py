# DRILL 1: DANIELA RECORRE EL CARTEL

cartel = [
    "Los Granados",
    "Cardumen",
    "La Sierra",
    "Espuma Fría",
    "Aurora Doble",
    "Vento Sur"
]

# Recorrer directamente cada banda e imprimir su anuncio
for banda in cartel:
    print(f"🎵 {banda} toca en SonidoLibre 2026")

# Mostrar el total después del bucle, sin indentación
print(f"Total de anuncios generados: {len(cartel)}")