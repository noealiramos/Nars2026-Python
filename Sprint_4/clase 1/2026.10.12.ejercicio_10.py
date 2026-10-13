ciudad = "aguascalientes" 
print(ciudad[::-1]) # nos imprime la palabra al revés

# ciudad[3] = "z" # nos da error porque las cadenas de texto son inmutables
# print(ciudad)

ciudad2=["a","g","u","a","s","c","a","l","i","e","n","t","e","s"] #este es un string
print(ciudad2[::-1])

ciudad2[3] = "z" # nos permite cambiar el valor de la lista porque las listas son mutables
print(ciudad2)