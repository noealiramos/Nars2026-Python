#reporte que muestre los años de servicio de empleados que entraron entre el 2018 al 2025 inclusive. Se debe imprimir cuantos años de antiguedad acumulan al cierre de 2025

#Reporte de antiguedad ► empleados ingresados entre el 2018 y el 2025 (incluyendolo)
anio_corte = int(input("cual es el anio de corte: "))
anio_ingreso = int(input("cual es el anio de ingreso: "))

print(f"Reporte de antiguedad al cierre {anio_corte}\n")

for anio_ingreso in range(anio_ingreso,anio_corte):
    antiguedad = anio_corte - anio_ingreso
    print(f"ingresó en {anio_ingreso}► {antiguedad} anios de antiguedad")