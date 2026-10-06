# EJERCICIO DEL AUTOCOMPLEMENTADOR DEL CODIGO, NO ES EL QUE HICIMOS EN CLASE

saldo = 1000
while True:
    print("\nSaldo actual:", saldo)
    print("Opciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        deposito = float(input("Ingrese el monto a depositar: "))

        if deposito > 0:
            saldo += deposito
            print(f"Se ha depositado {deposito}. Nuevo saldo: {saldo}")
        else:
            print("El depósito debe ser mayor a 0.")
        
    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))

        if retiro <= 0:
            print("El retiro debe ser mayor a 0.")

        elif retiro <= saldo:
            saldo -= retiro
            print(f"Se ha retirado {retiro}. Nuevo saldo: {saldo}")

        else:
            print("Saldo insuficiente para realizar el retiro.")
            
    elif opcion == "3":
        print("Saliendo del programa.")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")