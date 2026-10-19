# DRILL 5: EL FLYER REDUCIDO DE SOFÍA

cartel_completo = [
    "Los Granados",
    "Cardumen",
    "La Sierra",
    "Espuma Fría",
    "Aurora Doble",
    "Vento Sur",
    "Tornillos",
    "Lumbre Lenta"
]

# TODO 1: Obtiene las primeras 3 bandas.
headliners = cartel_completo[:3]

# TODO 2: Obtiene las últimas 3 bandas.
emergentes = cartel_completo[-3:]

# TODO 3: Imprime ambos grupos con su encabezado.
print(f"🎤 HEADLINERS: {headliners}")
print(f"🎸 EMERGENTES: {emergentes}")

# TODO 4: Muestra la lista original y comprueba su tamaño.
print(cartel_completo)
print(f"Total de bandas en el cartel original: {len(cartel_completo)}")