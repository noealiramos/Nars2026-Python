# DRILL 2: LA CALCULADORA DE PESOS DE VALENTINA

# TODO 1: Define una función llamada 'sumar_pesos' que reciba dos parámetros:
# 'peso_a' y 'peso_b'. Debe devolver con return la suma de ambos.
def sumar_pesos(peso_a, peso_b):
    return peso_a + peso_b


# TODO 2: Llama la función con 12.5 y 8.3, guarda el resultado en 'envio_1'.
envio_1 = sumar_pesos(12.5, 8.3)


# TODO 3: Llama la función otra vez con 25.0 y 17.5, guarda el resultado en 'envio_2'.
envio_2 = sumar_pesos(25.0, 17.5)


# TODO 4: Imprime ambos resultados con f-strings.
print(f"Peso del envío 1: {envio_1:.1f} kg")
print(f"Peso del envío 2: {envio_2:.1f} kg")


# TODO 5: BONUS — Llama a sumar_pesos pasando el resultado de las dos llamadas
# anteriores: sumar_pesos(envio_1, envio_2). Imprime el gran total.
gran_total = sumar_pesos(envio_1, envio_2)
print(f"Gran total: {gran_total:.1f} kg")