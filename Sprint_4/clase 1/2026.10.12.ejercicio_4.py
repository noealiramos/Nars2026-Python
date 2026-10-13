numeros = [10,20,30,40,50]

print(numeros[1:4]) #[20, 30, 40]
print(numeros[0:3]) #[10, 20, 30]
print(numeros[2:5]) #[30, 40, 50]

print(f"{'-'* 20}") #--------------------

print(numeros[1:]) #[20, 30, 40, 50]
print(numeros[:3]) #[10, 20, 30]

print(f"{'-'* 20}") #--------------------
print(numeros[::2]) #[10, 30, 50]
print(numeros[1::2]) #[20, 40]

print(f"{'-'* 20}") #--------------------
print(numeros[::-2]) #[50, 30, 10]

print(f"{'-'* 20}") #--------------------
print(numeros[3::-2]) #[40, 20]