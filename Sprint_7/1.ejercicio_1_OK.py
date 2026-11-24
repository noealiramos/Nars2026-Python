# while True:
#     try:
#         patrimonio = float(input("patrimonio de la empresa:"))
#         break
#     except ValueError:
#         print("[ERROR] Eso no es un numero, intentalo de nuevo")
        
# print("patrimonio aceptado: ", patrimonio)


while True:
    try:
        patrimonio = float(input("patrimonio de la empresa:"))
        print(type(patrimonio))
        patrimonio = float(patrimonio)
        break
    except ValueError:
        print("[ERROR] Eso no es un numero, intentalo de nuevo")
        
print("patrimonio aceptado: ", patrimonio)
