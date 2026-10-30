# Limpiador de Datos de Usuario

print("=== SISTEMA DE LIMPIEZA DE DATOS ===\n")


# TODO 1: Crea 4 variables con datos "sucios" tal como llegarían de un
# formulario (con espacios sobrantes, mayúsculas o guiones):
#   nombre_sucio, email_sucio, telefono_sucio, mensaje_sucio.
# Imprime "--- DATOS ORIGINALES ---" y muéstralas entre comillas.
nombre_sucio = "   juan carlos PÉREZ lópez   "
email_sucio = "  Juan.Perez@GMAIL.COM  "
telefono_sucio = "555-123-4567"
mensaje_sucio = "   HOLA, me gustaría recibir más información sobre el curso.   "

print("--- DATOS ORIGINALES ---")
print(f"Nombre:   '{nombre_sucio}'")
print(f"Email:    '{email_sucio}'")
print(f"Teléfono: '{telefono_sucio}'")
print(f"Mensaje:  '{mensaje_sucio}'")
print()


# TODO 2: Limpia cada dato y guárdalo en una variable nueva:
#   - nombre:   .strip().title()
#   - email:    .strip().lower()
#   - telefono: .replace("-", "")
#   - mensaje:  .strip().capitalize()
# Imprime "--- DATOS LIMPIOS ---" y muestra los resultados.
nombre_limpio = nombre_sucio.strip().title()
email_limpio = email_sucio.strip().lower()
telefono_limpio = telefono_sucio.replace("-", "")
mensaje_limpio = mensaje_sucio.strip().capitalize()

print("--- DATOS LIMPIOS ---")
print(f"Nombre:   '{nombre_limpio}'")
print(f"Email:    '{email_limpio}'")
print(f"Teléfono: '{telefono_limpio}'")
print(f"Mensaje:  '{mensaje_limpio}'")
print()


# TODO 3: Imprime "--- VALIDACIONES ---".
# Valida el email: comprueba que contiene "@" (con 'in') y que
# termina en ".com" (con .endswith()). Imprime ✅ o ❌.
print("--- VALIDACIONES ---")
if "@" in email_limpio and email_limpio.endswith(".com"):
    print("✅ Email válido")
else:
    print("❌ Email inválido")


# TODO 4: Valida el teléfono: debe tener 10 caracteres (len()) y ser
# todo dígitos (.isdigit()). Imprime ✅ o ❌.
if len(telefono_limpio) == 10 and telefono_limpio.isdigit():
    print("✅ Teléfono válido")
else:
    print("❌ Teléfono inválido")
print()


# TODO 5: Divide el mensaje en palabras con .split() e imprime cuántas
# palabras tiene usando len().
palabras = mensaje_limpio.split()
print(f"El mensaje tiene {len(palabras)} palabras")


# TODO 6: Separa el nombre completo con .split(). Si tiene 2 o más partes,
# toma la primera como primer_nombre y une el resto con " ".join() como
# apellido. Imprime ambos.
partes_nombre = nombre_limpio.split()
if len(partes_nombre) >= 2:
    primer_nombre = partes_nombre[0]
    apellido = " ".join(partes_nombre[1:])
    print(f"Primer nombre: {primer_nombre}")
    print(f"Apellido:      {apellido}")
else:
    print(f"Nombre: {nombre_limpio} (sin apellido)")


# TODO 7: Genera un username con email_limpio.split("@")[0] e imprímelo.
username = email_limpio.split("@")[0]
print(f"Username: {username}")
