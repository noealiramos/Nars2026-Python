def razon_endeudamiento(pasivos, patrimonio):
    try:
        return pasivos / patrimonio
    except ValueError:
        print("Error los valores no son validos")
        return -1
    except ZeroDivisionError:
        print("Error, el valor de patrimonio no puede ser cero")
        return -1

def margen_nomina(utilidad_operativa, costo_nomina):

    try:
        return utilidad_operativa / costo_nomina
    except ValueError:
        print("Error los valores no son validos")
        return -1
    except ZeroDivisionError:
        print("Error, el valor de costo nomina no puede ser cero")
        return -1

while True:        
    print(f"1) Razón de endeudamiento  (pasivos / patrimonio)\n")
    print(f"2) Margen sobre nómina      (utilidad_operativa / costo_nomina)\n")
    print(f"3) Salir")

    while True:
        try:
            opcion = int(input("Opcion: "))    
            if 1 <= opcion <= 3:
                break
        except ValueError:
            print("Opcion deber ser numerica")
             
    if opcion == 1:   #pedir los datos para razon endeudamiento
        while True:     
            try:
                pasivos = float(input("Entra cantidad pasivos: "))
                break
            except ValueError:
                print("Debe ser una cantidad numerica")

        #Ya tengo mi valor pasivos correcto
        while True:     
            try:
                patrimonio = float(input("Entra cantidad patrimonio: "))
                break
            except ValueError:
                print("Debe ser una cantidad numerica")
            finally:
                print("Bitacora: registro realizado")
                
        print(f"Razon de endeudamiento: {razon_endeudamiento(pasivos, patrimonio)}")
    elif opcion == 2:  #pedir los datos para margen sobre nomina
        while True:     
            try:
                utilidad = float(input("Entra cantidad utilidad: "))
                break
            except ValueError:
                print("Debe ser una cantidad numerica")

        #Ya tengo mi valor pasivos correcto
        while True:     
            try:
                costo = float(input("Entra cantidad costo: "))
                break
            except ValueError:
                print("Debe ser una cantidad numerica")
            finally:
                print("Bitacora: registro realizado")
                
        print(f"Margen sobre nomina: {margen_nomina(utilidad, costo)}")
    elif opcion == 3:
        break

print("Sesion terminada")
