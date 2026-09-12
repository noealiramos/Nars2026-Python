# print("2"+"2")     #►22
# print(2+2)         #►4
# print("ha"*3)       #►hahaha


#-------------------------------------------

# edad = input("Ingrese su edad: ") #tipo string
# edad = int(edad)
# edad = edad + 10

#-------------------------------------------

# print(f"Usted tiene {edad} años.")

# edad = int(input("Ingrese su edad: "))
# print(f"Usted tiene {edad+10} años.")
# sueldo = int(input("Ingrese su sueldo: "))
# print(f"Usted tiene {sueldo} pesos.")

# sueldo = float(input("Ingrese su sueldo: ")) 
# print(f"Usted tiene {sueldo} pesos. \
#     y va a tener un aumento del 10%: {sueldo*1.1} pesos.")


#-------------------------------------------
#PEDIR nombre, ano de nacimiento, sueldo
#IMPRIMIR gafete virtual, seguido de los datos

# print("----GAFETE VIRTUAL----")
# # Nombre
# # Edad
# # Sueldo

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))

# print(f"----GAFETE VIRTUAL----")
# #print(f"Nombre: {nombre.lower().capitalize()}") #► estamos dando formato al nombre para que se vea en minusculas
# print(f"Nombre: {nombre.title()}") #► estamos dando formato al nombre para que se vea en mayusculas y minusculas
# print(f"Edad: {edad}")
# print(f"Sueldo: {sueldo: .2f} pesos.") #► estamos dando formato al sueldo para que se vea con 2 decimales

#-------------------------------------------

# print(f"----GAFETE VIRTUAL----")
# print(f"{nombre=},{edad=},{sueldo=}")

#-------------------------------------------

print(f"----GAFETE VIRTUAL----")
print(f"Nombre:{nombre:^10}") #alt + 94 para la "^""


# #casting  ►►►
# int()
# float()
# :.2f
