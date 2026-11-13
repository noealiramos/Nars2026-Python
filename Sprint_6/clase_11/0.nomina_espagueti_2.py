"""
nomina_espagueti.py  — PUNTO DE PARTIDA (hay que refactorizar)
Procesa 3 empleados. La logica esta repetida y mezclada. Funciona, pero es fragil.
--- empleado 1 ---
sueldo1 = 20000
bono1 = 2000
bruto1 = sueldo1 + bono1
impuesto1 = bruto1 * 0.12
neto1 = bruto1 - impuesto1
print(f"Empleado 1 | Bruto: ${bruto1} | Impuesto: ${impuesto1} | Neto: ${neto1}")

--- empleado 2 ---
sueldo2 = 25000
bono2 = 0
bruto2 = sueldo2 + bono2
impuesto2 = bruto2 * 0.12
neto2 = bruto2 - impuesto2
print(f"Empleado 2 | Bruto: ${bruto2} | Impuesto: ${impuesto2} | Neto: ${neto2}")

--- empleado 3 ---
sueldo3 = 500          # OJO: salario sospechoso, pero el espagueti lo procesa igual
bono3 = 100
bruto3 = sueldo3 + bono3
impuesto3 = bruto3 * 0.12
neto3 = bruto3 - impuesto3
print(f"Empleado 3 | Bruto: ${bruto3} | Impuesto: ${impuesto3} | Neto: ${neto3}")
"""

"""Procesa la nómina y rechaza los sueldos fuera del rango permitido."""


"""
◄◄◄◄ CASOS NOMINA ►►►►

Cambia el empleado 3 a: sueldo 8000, bono 0

RESULTADO ESPERADO:
  Empleado 3 | Bruto: $8000 | Neto: $7040.0   (8000 es VALIDO, inclusive)
  NO debe decir RECHAZADO.

QUE DETECTA: si la validacion uso < en vez de <= (off-by-one en validacion).
Si el programa rechaza al de 8000, el autor uso el limite estricto.

Cambia los 3 sueldos a: 100, 200, 300 (bonos 0)

RESULTADO ESPERADO:
  3 lineas RECHAZADO
  Empleados procesados: 0
  Empleados rechazados: 3
  Total neto a depositar: $0     (cero, no None, no error)

QUE DETECTA: si el acumulador del total inicia mal o si el resumen
truena cuando nadie se procesa. Tambien si cuenta mal procesados/rechazados.

Deja los datos base, pero cambia tasa_impuesto a 0.20 (UNA sola linea).

RESULTADO ESPERADO:
  Empleado 1 | Bruto: $22000 | Neto: $17600.0
  Empleado 2 | Bruto: $25000 | Neto: $20000.0
  Total neto a depositar: $37600.0

QUE DETECTA: si la tasa estaba duplicada/hardcodeada en algun lado.
Si al cambiar una linea NO cambian todos los netos -> hay espagueti escondido.

Cambia el empleado 1 a: sueldo 9000, bono 50000

RESULTADO ESPERADO (con validacion sobre el SUELDO BASE, que es 9000, valido):
  Empleado 1 | Bruto: $59000 | Neto: $51920.0   (con tasa 0.12)

QUE DETECTA: si el autor valido el BRUTO en vez del SUELDO BASE.
La regla dice "salario" = sueldo_base. Si valido el bruto (59000) sigue
siendo valido aqui; pero la pregunta para el autor es: ¿que estas validando
exactamente, y es lo que pedia la especificacion?

◄◄◄◄ CASOS NOMINA ►►►►

"""


tasa_impuesto = 0.20
salario_minimo = 8000
salario_maximo = 200000


def es_salario_valido(salario): #Valida el sueldo base; ambos límites están incluidos
    return salario_minimo <= salario <= salario_maximo

def calcular_nomina(sueldo, bono, tasa_impuesto=tasa_impuesto): #Devuelve el bruto, el impuesto y el neto de un sueldo válido. #Devuelve el bruto, el impuesto y el neto de un sueldo válido.
    if not es_salario_valido(sueldo):
        raise ValueError(
            f"El sueldo debe estar entre ${salario_minimo:,.2f} "
            f"y ${salario_maximo:,.2f}."
        )

    bruto = sueldo + bono
    impuesto = bruto * tasa_impuesto
    neto = bruto - impuesto
    return bruto, impuesto, neto


def imprimir_recibo(nombre, bruto, impuesto, neto):
    #Muestra los importes con dos decimales.
    print(
        f"{nombre} | Bruto: ${bruto:,.2f} | "
        f"Impuesto: ${impuesto:,.2f} | Neto: ${neto:,.2f}"
    )


def main():
    empleados = [
        {"nombre": "Empleado 1", "sueldo": 9000 , "bono": 0},
        {"nombre": "Empleado 2", "sueldo": 200, "bono": 0},
        {"nombre": "Empleado 3", "sueldo": 300, "bono": 100},
    ]

    empleados_procesados = 0
    empleados_rechazados = 0
    total_neto = 0

    print(f"VALORES ESPERADOS (config base)") #titulo de la tabla

    for empleado in empleados:
        try:
            bruto, impuesto, neto = calcular_nomina(
                empleado["sueldo"], empleado["bono"]
            )
        except ValueError as error:
            empleados_rechazados += 1
            print(f"{empleado['nombre']} | RECHAZADO: {error}")
            continue

        empleados_procesados += 1
        total_neto += neto
        imprimir_recibo(empleado["nombre"], bruto, impuesto, neto)

    print(f"\nEmpleados procesados: {empleados_procesados}")
    print(f"Empleados rechazados: {empleados_rechazados}")
    print(f"Total neto a depositar = ${total_neto:,.2f}")


if __name__ == "__main__":
    main()
