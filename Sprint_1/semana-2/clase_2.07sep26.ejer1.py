# print("2"+"2")     #►22
# print(2+2)         #►4
# print("ha"*3)       #►hahaha


edad = input("Ingrese su edad: ") #tipo string
print(type(edad))               #para saber el tipo de dato que es la variable edad

edad = int(edad)
print(type(edad))

edad = edad + 10
print(type(edad))

print(f"Usted tiene {edad} años.")