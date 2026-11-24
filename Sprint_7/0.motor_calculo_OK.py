def calcular_raon(pasivos, patrimonio):
    try:
        razon = pasivos / patrimonio
        return razon
    except ValueError:
        return "Dato invalido"
    except ZeroDivisionError:
        return "el patrimonio NO se puede dividir entre cero"
    except TypeError:
        return "los valores deben ser numericos"
    finally:
        print("Cálculo intentado")
        
    print(calcular_razon("hola", 0))  
    