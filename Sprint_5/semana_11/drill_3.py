# DRILL 3: BUSCAR Y REEMPLAZAR — EL CAMBIO DE NOMBRE DE DANIELA

# TODO 1: Crea una variable llamada 'comunicado' con este texto:
# "El Escenario Secundario abre a las 18h. Los artistas del Escenario Secundario
#  deben presentarse 30 minutos antes."
comunicado = "El Escenario Secundario abre a las 18h. Los artistas del Escenario Secundario deben presentarse 30 minutos antes."

# TODO 2: Usa .replace() para cambiar "Escenario Secundario" por "Escenario Granado".
# Guarda el resultado en una variable llamada 'comunicado_actualizado'.
comunicado_actualizado = comunicado.replace("Escenario Secundario", "Escenario Granado")

# TODO 3: Imprime ambas versiones (original y actualizada) para confirmar el cambio.
print(f"Original:    {comunicado}")
print(f"Actualizado: {comunicado_actualizado}")

# TODO 4: ¿Qué pasa si intentas reemplazar una palabra que NO existe en el texto?
# Prueba: comunicado.replace("Coachella", "SonidoLibre")
# Imprime el resultado y verifica que no haya error.
print(comunicado.replace("Coachella", "SonidoLibre"))