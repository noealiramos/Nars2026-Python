# DRILL 3: EL RADAR DE LUCÍA

# TODO 1: Diccionario con tres medios
medios_acreditados = {
    "Diario del Sur": True,
    "Radio Granado": True,
    "Revista Eco": True
}

# TODO 2: Pedir el nombre del medio
medio_buscado = input("¿Qué medio quieres verificar? ")

# TODO 3: Verificar con 'in'
if medio_buscado in medios_acreditados:
    print(f"{medio_buscado} ya está acreditado.")
else:
    print(f"{medio_buscado} aún no figura en el registro.")