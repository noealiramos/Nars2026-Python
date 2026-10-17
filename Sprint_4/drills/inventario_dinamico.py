# INVENTARIO DINÁMICO

# TODO 1: Crear una lista vacía.
inventario = []

# TODO 2: Imprimir el encabezado.
print("=== Inventario Dinámico ===")

# TODO 3: Agregar tres productos en orden.
inventario.append("Laptop")
inventario.append("Mouse")
inventario.append("Teclado")
print(f"Inventario actual: {inventario}")

# TODO 4: Insertar Monitor en la primera posición.
inventario.insert(0, "Monitor")
print(f"Inventario después de insertar Monitor: {inventario}")

# TODO 5: Eliminar el último producto y guardar su valor.
ultimo = inventario.pop()
print(f"Producto eliminado: {ultimo}")
print(f"Inventario después de pop(): {inventario}")

# TODO 6: Eliminar Mouse por su nombre.
inventario.remove("Mouse")
print(f"Inventario después de eliminar Mouse: {inventario}")

# TODO 7: Mostrar el total de productos restantes.
print(f"Total de productos restantes: {len(inventario)}")

# TODO 8: Recorrer e imprimir cada producto.
for producto in inventario:
    print(f"- {producto}")