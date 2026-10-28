persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])  # "Ana"
print(persona["edad"])    # 25
print(persona["ciudad"])  


#Modificar valores
persona["edad"] = 26
print(persona["edad"])  # 26

#Agregar nuevas claves
persona["email"] = "ana@example.com"
print(persona)  # {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid', 'email': 'ana@example.com'}