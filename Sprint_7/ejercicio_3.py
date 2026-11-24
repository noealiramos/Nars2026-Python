try:
    eddad = inch("treinta")
    total = 100 / 0
    mensaje = "salarios" + 5000
except ValueError:
    print("value error detectado")
except ZeroDivisionError:
    print("el patrimonio NO se puede dividir entre cero")
except TypeError:
    print("huno un error de tipo")    