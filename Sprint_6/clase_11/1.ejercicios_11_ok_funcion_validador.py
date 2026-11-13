#mini drill 7
# #temer ima ñosta de 4 sañarops. ´pr cada uno imprime "procesas": <salario> si es valido, o rechar: <salario> si no:

# 20000, 500, 20000,25000

# salida esperada:
#     PROCESAR: 20000
#     RECHAZAR: 500
#     PROCESAR: 20000
#     RECHAZAR: 25000

lista_salarios = [20000, 500, 20000, 25000]

for salario in lista_salarios:
    def es_salario_valido(salario):
        ...

    es_valido = es_salario_valido(salario)
    
    if es_valido:
        print(f"PROCESAR: {salario}")
    else:
        print(f"RECHAZAR: {salario}")
    
    