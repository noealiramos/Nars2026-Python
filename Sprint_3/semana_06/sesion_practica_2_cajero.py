# CAJERO — el motor que no se apaga hasta que el usuario decide

# TODO 1: Escribe un bucle 'while True:' que mantenga el cajero encendido.

  # TODO 2: Dentro del bucle, imprime el menú con estas líneas:
  #   "Menú"
  #   "1) Consultar saldo"
  #   "2) Salir"


  # TODO 3: Pide la opción del usuario con input("Elige una opción: ")
  # y guárdala en una variable 'opcion'.
  # IMPORTANTE: NO la conviertas a int — déjala como string.


  # TODO 4: Si la opción NO está dentro de la lista ["1", "2"],
  # imprime "Opción no válida. Intenta de nuevo. Elige entre 1 y 2."
  # y usa 'continue' para volver al menú sin procesar el resto.


  # TODO 5: Si la opción es "1", imprime "Tu saldo es de 1000."


  # TODO 6: Si la opción es "2", imprime "Hasta luego."
  # y usa 'break' para salir del bucle.

# CAJERO — el motor que no se apaga hasta que el usuario decide

while True:
    print("Menú")
    print("1) Consultar saldo")
    print("2) Salir")

    opcion = input("Elige una opción: ")

    if opcion not in ["1", "2"]:
        print("Opción no válida. Intenta de nuevo. Elige entre 1 y 2.")
        continue

    if opcion == "1":
        print("Tu saldo es de 1000.")

    elif opcion == "2":
        print("Hasta luego.")
        break
