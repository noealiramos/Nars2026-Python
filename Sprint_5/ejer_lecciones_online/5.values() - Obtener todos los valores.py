#2. .values() - Obtener todos los valores

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
claves = persona.keys()


valores = persona.values()
print(valores)  # dict_values(['Ana', 25, 'Madrid'])

# Iterar sobre los valores
for valor in persona.values():
    print(valor)
    
    
    
    
    
print("====3. .items() - Obtener pares clave-valor=========")

items = persona.items()
print(items)  # dict_items([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Madrid')])

# Iterar sobre pares (MUY ÚTIL)
for clave, valor in persona.items():
    print(f"{clave}: {valor}")