try:
   patrimonio = float(input("patrimonio de la empresa: "))
   pasivos = float(input("pasivos de la empresa: "))
   razon = pasivos / patrimonio
   print("razon de endeudamiento: ", round(razon,2)) 
   

except ValueError:
    print("[ERROR] eso no es un numer, usa digitos dentro del o 80000")
except ZeroDivisionError:
    print("[ERROR] El patrimonio no puede ser cero ")
except Exception: # se va ejecutar siempre que haya un error
    print("[Error] hubo un errorr de desconocido")
else:
    print("razon de endeudaminto: ",round(razon,2))
    print("[ok] calculo exitoso")
finally:
    print("[bitacora] intento de calculo registrado")
    
    