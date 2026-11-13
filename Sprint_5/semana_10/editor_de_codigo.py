# Formulario de Registro - Sprint 5 Práctica
 
print("=== FORMULARIO DE REGISTRO DE RECLUTA ===\n")
 
datos_sucios = {
  "nombre": "  CARLOS   RUIZ  ",
  "email": "  CARLOS.RUIZ@EXAMPLE.COM  ",
  "telefono": "555-123-4567",
  "edad": "25",
  "ciudad": "madrid"
}
 
print("--- DATOS RECIBIDOS (SUCIOS) ---")
for campo, valor in datos_sucios.items():
  print(f"{campo}: '{valor}'")
 
# TODO 1: Crea un diccionario vacío 'datos_limpios' y limpia cada campo:
#   - nombre: .strip(), luego .split() y " ".join() para quitar espacios dobles,
#             luego .title()
#   - email: .strip().lower()
#   - telefono: elimina "-", "(", ")", ".", " " con .replace() (uno por uno)
#   - edad: .strip()
#   - ciudad: .strip().title()
# Imprime datos_limpios con el mismo formato de arriba.
datos_limpios = {}
 
nombre = datos_sucios["nombre"].strip()
nombre = " ".join(nombre.split())
datos_limpios["nombre"] = nombre.title()
 
datos_limpios["email"] = datos_sucios["email"].strip().lower()
 
telefono = datos_sucios["telefono"]
telefono = telefono.replace("-", "")
telefono = telefono.replace("(", "")
telefono = telefono.replace(")", "")
telefono = telefono.replace(".", "")
telefono = telefono.replace(" ", "")
datos_limpios["telefono"] = telefono
 
datos_limpios["edad"] = datos_sucios["edad"].strip()
datos_limpios["ciudad"] = datos_sucios["ciudad"].strip().title()
 
print("\n--- DATOS LIMPIOS ---")
for campo, valor in datos_limpios.items():
  print(f"{campo}: '{valor}'")
 
 
# TODO 2: Crea una lista vacía 'errores' y valida cada campo:
#   - nombre: len(datos_limpios["nombre"].split()) < 2 → error "Nombre debe incluir apellido"
#   - email: debe contener "@" y "." en el dominio → error si no
#   - telefono: .isdigit() y len() == 10 → error si no
#   - edad: .isdigit() → si pasa, convierte a int y verifica 18 <= edad <= 100
# Por cada campo que pase, imprime "✅ [campo] válido".
# Por cada campo que no pase, agrega el mensaje de error a 'errores'.
errores = []
print("\n--- VALIDACIÓN ---")
 
if len(datos_limpios["nombre"].split()) < 2:
  errores.append("Nombre debe incluir apellido")
else:
  print("✅ nombre válido")
 
email = datos_limpios["email"]
if "@" in email and "." in email.split("@")[-1]:
  print("✅ email válido")
else:
  errores.append("Email debe contener '@' y '.' en el dominio")
 
tel = datos_limpios["telefono"]
if tel.isdigit() and len(tel) == 10:
  print("✅ telefono válido")
else:
  errores.append("Teléfono debe tener exactamente 10 dígitos")
 
if datos_limpios["edad"].isdigit():
  edad = int(datos_limpios["edad"])
  if 18 <= edad <= 100:
    datos_limpios["edad"] = edad
    print("✅ edad válido")
  else:
    errores.append("Edad debe estar entre 18 y 100")
else:
  errores.append("Edad debe ser un número")
 
 
# TODO 3: Si 'errores' está vacío, imprime "--- REGISTRO EXITOSO ---"
# y muestra cada campo (nombre a la izquierda en 15 chars, valor en 30 chars).
# Formatea también el teléfono como "(555) 123-4567" usando slicing.
# Si hay errores, imprime "--- REGISTRO RECHAZADO ---" y lista cada error.
if not errores:
  print("\n--- REGISTRO EXITOSO ---")
  tel = datos_limpios["telefono"]
  datos_limpios["telefono"] = f"({tel[:3]}) {tel[3:6]}-{tel[6:]}"
  for campo, valor in datos_limpios.items():
    print(f"{campo:<15}{str(valor):<30}")
else:
  print("\n--- REGISTRO RECHAZADO ---")
  for error in errores:
    print(f"❌ {error}")