try:
   patrimonio = float(input("patrimonio de la empresa: "))
   pasivos = float(input("pasivos de la empresa: "))
   razon = pasivos / patrimonio
   print("razon de endeudamiento: ", round(razon,2)) 
   
except Exception: # se va ejecutar siempre que haya un error
    print("[Error] - Exception-  hubo un errorr de desconocido")
except ValueError:
    print("[ERROR] - ValueError- eso no es un numero, usa digitos dentro del o 80000")
except ZeroDivisionError:
    print("[ERROR] -ZeroDivisionError - El patrimonio no puede ser cero ")

