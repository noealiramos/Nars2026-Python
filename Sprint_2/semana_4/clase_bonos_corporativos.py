categoria = input("categoria del empleado (a/b/c): ")
años_sevicio = int(input("años de servicio: "))
evaluacion = float(input("calificaciones de evaluacion (0-100): "))

if categoria == "A":
    if años_sevicio >= 5:
        if evaluacion >= 80:
            print("Bono maximo: 20%")
        else:
            print("bono estandar : 10%")
    else:    
        print("sin elegibilidad aun (menos de 5 años)")
elif categoria =="B":
    if evaluacion >=90:
        print("bono por desempleao excepcional: 15% ")
    else:
        print("bono base: 5%")
else:
    print("categoria sin esquema de bonos definido")
    
    
    # Meta = el programa debe impprimir por estos inputs:
    # categoria ="A", años =  6, evaluacion = 85 , "bono maximo: 20%"
    # categoria ="A", años =  3, evaluacion = 95 , "sin elegibilidad aun (menos de 5años)"
    # categoria ="B", años = cualquiera, evaluacion = 92 , "bono por desempeño excepcional: 15%"
    # categoria ="C", cualquiercosa , categoria sin esquema de bonos definido
    
    
    
# categoria = input("Categoría del empleado (A/B/C): ").upper()

# anios_servicio = int(input("Años de servicio: "))

# evaluacion = float(input("Calificación de evaluación (0-100): "))


# if categoria == "A":

#     if anios_servicio >= 5:

#         if evaluacion >= 80:
#             print("Bono máximo: 20%")
#         else:
#             print("Bono estándar: 10%")

#     else:
#         print("Sin elegibilidad aún (menos de 5 años)")


# elif categoria == "B":

#     if evaluacion >= 90:
#         print("Bono por desempeño excepcional: 15%")
#     else:
#         print("Bono base: 5%")


# else:
#     print("Categoría sin esquema de bonos definido")