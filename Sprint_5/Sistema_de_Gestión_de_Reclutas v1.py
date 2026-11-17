# Sistema de Gestión de Reclutas - Sprint 5 ENTREGABLE

print("=== SISTEMA DE GESTIÓN DE RECLUTAS ===\n")

reclutas = [
  {"nombre": "Ana López", "edad": 25, "email": "ana@example.com", "rango": "Aprendiz", "puntos": 200},
  {"nombre": "Luis García", "edad": 30, "email": "luis@example.com", "rango": "Experto", "puntos": 500},
  {"nombre": "Carlos Ruiz", "edad": 22, "email": "carlos@example.com", "rango": "Novato", "puntos": 100}
]

# TODO 1: Define limpiar_string(texto).
# Retorna el texto sin espacios extremos (.strip()).
def limpiar_string(texto):
  return texto.strip()

# TODO 2: Define validar_email(email).
# Limpia el email con .strip().lower().
# Retorna True si contiene "@" y el dominio (parte después del "@") tiene ".".
def validar_email(email):
  email = email.strip().lower()
  if "@" not in email:
    return False
  dominio = email.split("@")[-1]
  return "." in dominio

# TODO 3: Define dar_alta_recluta().
# Pide: nombre, edad (str), email con input().
# Valida que edad.isdigit() y que 18 <= int(edad) <= 100; si no, imprime error y retorna.
# Valida el email con validar_email(); si no, imprime error y retorna.
# Limpia nombre con limpiar_string().title() y email con .strip().lower().
# Arma el diccionario con nombre, edad (int), email, rango="Novato", puntos=0.
# Agrega a reclutas con .append() e imprime confirmación.
def dar_alta_recluta():
  print("\n--- ALTA DE RECLUTA ---")
  nombre = input("Nombre: ")
  edad = input("Edad: ").strip()
  email = input("Email: ")

  if not edad.isdigit() or not (18 <= int(edad) <= 100):
    print("❌ Error: la edad debe ser un número entre 18 y 100.")
    return

  if not validar_email(email):
    print("❌ Error: el email no es válido.")
    return

  nombre = limpiar_string(nombre).title()
  email = email.strip().lower()

  nuevo = {
    "nombre": nombre,
    "edad": int(edad),
    "email": email,
    "rango": "Novato",
    "puntos": 0
  }
  reclutas.append(nuevo)
  print(f"✅ Recluta '{nombre}' dado de alta correctamente.")

# TODO 4: Define listar_reclutas().
# Si reclutas está vacío, avisa y retorna.
# Imprime encabezado: "#" (4), "Nombre" (20), "Edad" (6), "Rango" (12), "Puntos" (8)
# Imprime separadora de "-" * 52.
# Recorre reclutas con enumerate(reclutas, 1) y muestra cada fila alineada,
# con puntos formateados con :>8, (separador de miles).
# Imprime el total al final.
def listar_reclutas():
  if not reclutas:
    print("\nNo hay reclutas registrados.")
    return

  print("\n--- LISTA DE RECLUTAS ---")
  print(f"{'#':<4}{'Nombre':<20}{'Edad':<6}{'Rango':<12}{'Puntos':>8}")
  print("-" * 52)
  for i, recluta in enumerate(reclutas, 1):
    print(f"{i:<4}{recluta['nombre']:<20}{recluta['edad']:<6}"
          f"{recluta['rango']:<12}{recluta['puntos']:>8,}")
  print("-" * 52)
  print(f"Total: {len(reclutas)} reclutas")

# TODO 5: Define buscar_recluta().
# Pide un término con input() y normaliza con .strip().lower().
# Busca el término en recluta["nombre"].lower() usando 'in' (búsqueda parcial).
# Si no encontró nada, avisa. Si sí, imprime nombre, email y rango de cada resultado.
def buscar_recluta():
  print("\n--- BUSCAR RECLUTA ---")
  termino = input("Nombre a buscar: ").strip().lower()

  encontrados = []
  for recluta in reclutas:
    if termino in recluta["nombre"].lower():
      encontrados.append(recluta)

  if not encontrados:
    print(f"No se encontraron reclutas con '{termino}'.")
    return

  print(f"Se encontraron {len(encontrados)} resultado(s):")
  for recluta in encontrados:
    print(f"  • {recluta['nombre']} | {recluta['email']} | {recluta['rango']}")

# TODO 6: Define actualizar_puntos().
# Muestra la lista numerada de reclutas con sus puntos actuales.
# Pide selección numérica; valida con .isdigit() y que el índice esté en rango.
# Pide puntos a agregar (permite negativos: valida con puntos_str.lstrip("-").isdigit()).
# Suma con += al recluta seleccionado e imprime confirmación.
def actualizar_puntos():
  if not reclutas:
    print("\nNo hay reclutas registrados.")
    return

  print("\n--- ACTUALIZAR PUNTOS ---")
  for i, recluta in enumerate(reclutas, 1):
    print(f"{i}. {recluta['nombre']} - {recluta['puntos']:,} puntos")

  seleccion = input("Número de recluta: ").strip()
  if not seleccion.isdigit():
    print("❌ Error: debes escribir un número.")
    return

  indice = int(seleccion) - 1
  if not (0 <= indice < len(reclutas)):
    print("❌ Error: ese número no está en la lista.")
    return

  puntos_str = input("Puntos a agregar (usa - para restar): ").strip()
  if not puntos_str.lstrip("-").isdigit():
    print("❌ Error: los puntos deben ser un número entero.")
    return

  recluta = reclutas[indice]
  recluta["puntos"] += int(puntos_str)
  print(f"✅ {recluta['nombre']} ahora tiene {recluta['puntos']:,} puntos.")

# TODO 7: Define mostrar_estadisticas().
# Si reclutas está vacío, avisa y retorna.
# Calcula: total, puntos_totales (usa sum()), promedio.
# Encuentra el top con max(reclutas, key=lambda r: r["puntos"]).
# Cuenta por rango con el patrón: rangos[rango] = rangos.get(rango, 0) + 1
# Imprime todo de forma legible.
def mostrar_estadisticas():
  if not reclutas:
    print("\nNo hay reclutas registrados.")
    return

  total = len(reclutas)
  puntos_totales = sum(r["puntos"] for r in reclutas)
  promedio = puntos_totales / total
  top = max(reclutas, key=lambda r: r["puntos"])

  rangos = {}
  for recluta in reclutas:
    rango = recluta["rango"]
    rangos[rango] = rangos.get(rango, 0) + 1

  print("\n--- ESTADÍSTICAS ---")
  print(f"Total de reclutas:  {total}")
  print(f"Puntos totales:     {puntos_totales:,}")
  print(f"Promedio de puntos: {promedio:,.2f}")
  print(f"Top recluta:        {top['nombre']} ({top['puntos']:,} puntos)")
  print("Reclutas por rango:")
  for rango, cantidad in rangos.items():
    print(f"  - {rango}: {cantidad}")

# TODO 8: Implementa el menú principal con while True.
# Imprime 6 opciones: Alta, Listar, Buscar, Actualizar, Estadísticas, Salir.
# Lee la opción con input().strip() y llama a la función correspondiente.
# La opción "6" imprime despedida y hace break.
# Cualquier otra opción muestra un mensaje de error.
while True:
  print("\n========== MENÚ ==========")
  print("1. Alta de recluta")
  print("2. Listar todos")
  print("3. Buscar por nombre")
  print("4. Actualizar puntos")
  print("5. Estadísticas")
  print("6. Salir")
  opcion = input("Elige una opción: ").strip()

  if opcion == "1":
    dar_alta_recluta()
  elif opcion == "2":
    listar_reclutas()
  elif opcion == "3":
    buscar_recluta()
  elif opcion == "4":
    actualizar_puntos()
  elif opcion == "5":
    mostrar_estadisticas()
  elif opcion == "6":
    print("\n¡Hasta luego!!!")
    break
  else:
    print("❌ Opción no válida. Elige un número del 1 al 6.")