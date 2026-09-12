# ciudad
# temperatura en grados celsius

# Ciudad
# Celsius
# Fahrenheit
# Kelvin

# dos digitos decimales, cada valor

# Fah... = celcius * 9/5 + 32
# Kel... celcius + 273.15

ciudad = input("Ingrese la ciudad: ")
celsius = float(input("Ingrese la temp en celcius: "))

fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15

print(f"Ciudad: {ciudad.title()}")
print(f"Temp en Celsius: {celsius:.2f}°C")
print(f"Temp en Fahrenheit: {fahrenheit:.2f}°F")
print(f"Temp en Kelvin: {kelvin:.2f}°K")

