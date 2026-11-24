#PARA SABER cuales son los metodos que trae una libreria??

import os
ruta_actual = os.getcwd() #para saber donde estoy parado - para conocer mi ruta de trabajo, se puede guardar en una variable "current work directory"
print(f"tu directorio es: {ruta_actual}")


#para buscar si está o no un archivo. SI EXISTE enviará un TRUE, sino pues un FALSE

#nombre_archivo="prueba.txt"
nombre_archivo="\sprint_1\pruebas"
if os.path.exists(nombre_archivo):
    print("EL archivo existe")
else:
    print("EL archivo NO existe")