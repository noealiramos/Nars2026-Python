pasivos = 800000
patrimonio = 0

try:
    razon = pasivos / patrimonio
    print("razon de endeudamiento: ",razon)
except ZeroDivisionError:
    print("[error] el  patrimonio no puede ser ver, revisa el dato")

