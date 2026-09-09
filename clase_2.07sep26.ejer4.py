edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))
nombre = input("Ingrese su nombre: ")

resumen =f"Mediante esta carta, confirmamos que el sr {nombre.title()} de {edad} años, percibe un sueldo de {sueldo: .2f} pesos."

#str(edad)  ►►► para convertir un entero a string
#str(sueldo) ►►► para convertir un float a string

resumen2 ="Mediante esta carta, confirmamos que el sr "+ nombre.title() + " de " + str(edad) + " años, percibe un sueldo de " + str(sueldo) + " pesos."



print(f"{resumen=}")
print(f"{resumen2=}")