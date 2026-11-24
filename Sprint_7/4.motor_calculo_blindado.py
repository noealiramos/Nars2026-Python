# Regla de oro: el motor NO se puede caer NUNCA.
# Estructura: try / except / else / finally

import os
from datetime import datetime
archivo_bitacora = "bitacora_motor.txt"

# ----------------------------------------------------------
# Bitacora: registra cada intento (se llama desde finally)
# ----------------------------------------------------------

def registrar_intento(operacion, estado):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha}] {operacion} -> {estado}\n"
    with open(archivo_bitacora, "a", encoding="utf-8") as bitacora:
        bitacora.write(linea)
    print(f"   (bitacora) Intento registrado: {operacion} -> {estado}")


# ----------------------------------------------------------
# "Loop de acero"► no avanza hasta recibir un numero valido
# ----------------------------------------------------------
def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Error: eso no es un numero, usa solo digitos (ej. 80000).")
        else:
            return valor

def razon_endeudamiento():
    estado = "SIN COMPLETAR"
    try:
        pasivos = pedir_numero("Pasivos: ")
        patrimonio = pedir_numero("Patrimonio: ")
        resultado = pasivos / patrimonio
    except ValueError:
        estado = "ERROR ValueError"
        print("Error: se recibio un valor no numerico.")
    except ZeroDivisionError:
        estado = "ERROR ZeroDivisionError"
        print("Error: el patrimonio no puede ser 0. No se puede calcular la razon.")
    else:
        estado = f"OK ({round(resultado, 2)})"
        print(f"Razon de endeudamiento: {round(resultado, 2)}")
    finally:
        registrar_intento("Razon de endeudamiento", estado)


def margen_sobre_nomina():
    estado = "SIN COMPLETAR"
    try:
        utilidad_operativa = pedir_numero("Utilidad operativa: ")
        costo_nomina = pedir_numero("Costo de nomina: ")
        resultado = utilidad_operativa / costo_nomina
    except ValueError:
        estado = "ERROR ValueError"
        print("Error: se recibio un valor no numerico.")
    except ZeroDivisionError:
        estado = "ERROR ZeroDivisionError"
        print("Error: el costo de nomina no puede ser 0. No se puede calcular el margen.")
    else:
        estado = f"OK ({round(resultado, 2)})"
        print(f"Margen sobre nomina: {round(resultado, 2)}")
    finally:
        registrar_intento("Margen sobre nomina", estado)


# ----------------------------------------------------------
# Encabezado del programa
# ----------------------------------------------------------
def mostrar_encabezado():
    print("=" * 50)
    print("   MOTOR DE INDICADORES FINANCIEROS - RIESGO")
    print("=" * 50)


# ----------------------------------------------------------
# Requisito os: mostrar carpeta actual y verificar la bitacora
# ----------------------------------------------------------
def verificar_bitacora():
    print(f"* Directorio de trabajo: {os.getcwd()}")
    if os.path.exists(archivo_bitacora):
        print(f"* La bitacora '{archivo_bitacora}' ya existe. Se agregaran registros.")
    else:
        print(f"La bitacora '{archivo_bitacora}' no existe. Se creara en el primer intento.")


# ----------------------------------------------------------
# Menu: muestra las opciones y regresa la opcion elegida
# ----------------------------------------------------------
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1) Razon de endeudamiento  (pasivos / patrimonio)")
    print("2) Margen sobre nomina     (utilidad_operativa / costo_nomina)")
    print("3) Salir")
    opcion = input("Elige una opcion: ").strip()
    return opcion


# llamar las funciones
mostrar_encabezado()
verificar_bitacora()

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        razon_endeudamiento()
    elif opcion == "2":
        margen_sobre_nomina()
    elif opcion == "3":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida. Elige 1, 2 o 3 solamente")
