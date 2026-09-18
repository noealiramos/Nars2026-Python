
promedio = float(input("¿Cuál es tu promedio? "))
es_deportista = input("¿Eres un deportista destacado (sí/no)? ")
sin_reportes = input("¿Tienes reportes de indisciplina? (sí/no): ")

if (promedio > 85 or es_deportista == "sí") and sin_reportes == "no":
    print("Beca otorgada. ¡Felicidades!")