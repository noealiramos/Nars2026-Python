# GESTOR DE NOMBRES — ÍNDICES, SLICING Y BÚSQUEDA

# TODO 1: Crear la lista con los 7 nombres en orden.
nombres = ["Ana", "Luis", "Carlos", "María", "Pedro", "Sofía", "Diego"]

# TODO 2: Mostrar la lista completa y el total.
print("=== Lista Completa ===")
print(nombres)
print(f"Total de nombres: {len(nombres)}")

# ===== ACCESO POR ÍNDICE =====

# TODO 3: Mostrar el primer, último y tercer nombre.
print("\n=== Acceso por Índice ===")
print(f"Primer nombre: {nombres[0]}")
print(f"Último nombre: {nombres[-1]}")
print(f"Tercer nombre: {nombres[2]}")

# ===== SLICING =====

# TODO 4: Extraer y mostrar las cuatro sublistas.
print("\n=== Slicing ===")
print(f"Primeros 3 nombres: {nombres[:3]}")
print(f"Últimos 2 nombres: {nombres[-2:]}")
print(f"Del segundo al quinto: {nombres[1:5]}")
print(f"Todos menos el primero y el último: {nombres[1:-1]}")

# ===== BÚSQUEDA =====

# TODO 5: Verificar si Carlos existe y mostrar su índice.
print("\n=== Búsqueda ===")
buscar = "Carlos"

if buscar in nombres:
    posicion = nombres.index(buscar)
    print(f"{buscar} está en el índice {posicion}.")
else:
    print(f"{buscar} no está en la lista.")

# TODO 6: Agregar Roberto solamente si no existe.
nuevo = "Roberto"

if nuevo not in nombres:
    nombres.append(nuevo)
    print(f"Se agregó a {nuevo}.")
    print(f"Lista actualizada: {nombres}")
else:
    print(f"{nuevo} ya existe en la lista.")