# Sin .get() - lanza KeyError si no existe

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

print(persona["telefono"])  # ❌ KeyError

# Con .get() - devuelve None (o valor por defecto) si no existe
print(persona.get("telefono"))  # None
print(persona.get("telefono", "No disponible"))  # "No disponible"



print("=====5. .pop() - Eliminar clave y devolver valor=====")

ciudad = persona.pop("ciudad")
print(ciudad)  # "Madrid"
print(persona)  # {'nombre': 'Ana', 'edad': 25}