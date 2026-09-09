nombre = input('Cuál es tu nombre? ')
año_de_nacmiento = int(input('Cuál es tu año de nacimiento? '))
sueldo = float(input('Cuál es tu salario deseado? '))

año_actual = 2026

edad = año_actual - año_de_nacmiento

print("===== GAFETE VIRTUAL =====")
print(f"Nombre:     {nombre}")
print(f"Edad:        {edad} años")
print(f"Sueldo:       ${sueldo:.2f} MXN")
print(f"En 10 años tendrás {edad + 10}")
print("===========================")