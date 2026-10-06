

nombre = input("Ingrese su nombre: ")
print(f"*{'-' * len(nombre)}*\n")
print(f"[{nombre}]") 

linea_de_abajo=""
for i in range(len(nombre)):
    if i ==0:
        linea_de_abajo += "-" #EN UN STRING += LE AÑADE, LE CONTATENA
        print(f"-")
    elif i == len(nombre):
        print(f"x")
    else:
        print(f"|")