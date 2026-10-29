# Opción 1: Verificar si existe

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "telefono":"4491237787"}

if "telefono" in persona:
    print(persona["telefono"])
else:
    print("No tiene teléfono")

# Opción 2: Usar .get() con valor por defecto
telefono = persona.get("telefono", "Sin teléfono")
print(telefono)