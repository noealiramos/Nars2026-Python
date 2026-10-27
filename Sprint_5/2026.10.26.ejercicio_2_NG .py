empleado = {"nombre": "aana garcía", "departamento": "finazas"}
            
print("procesamiento de pago de: ", empleado ["nombre"])
print("salario a depostiar: ", empleado ["salario"])

empleado["salario"]

print(empleado.get("salario","no existe")) #va a buscar en el direccionar si exise el atributo y llave, y al no estar nos va a regresar un nnombre

empleado.get("salario",0)

print("nombre" in empleado)
print("departamento" in empleado)
print("finanzas" in empleado)
print("salario" in empleado)

