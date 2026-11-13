# Caso 2: Validar y Normalizar Email

print("=== VALIDACIÓN Y LIMPIEZA DE EMAILS ===\n")

emails_test = [
  "  ANA.LOPEZ@EXAMPLE.COM  ",
  "juan@gmail.com",
  "MARIA@HOTMAIL.COM",
  "pedro@",
  "carlosexample.com",
  "  luis@YAHOO.com  "
]

# TODO 1: Define limpiar_email(email).
# Retorna el email sin espacios extremos y en minúsculas.
def limpiar_email(email):
  return email.strip().lower()

# TODO 2: Define validar_email(email).
# Un email válido debe:
#   - Contener "@"
#   - Tener texto antes del "@" (parte local no vacía)
#   - Tener texto después del "@" (dominio no vacío)
#   - El dominio debe contener al menos un "."
# Retorna True si cumple todo, False si no.
def validar_email(email):
  if "@" not in email:
    return False

  local, dominio = email.split("@", 1)

  if local == "":
    return False
  if dominio == "":
    return False
  if "." not in dominio:
    return False

  return True

# TODO 3: Recorre emails_test.
# Para cada uno: limpia con limpiar_email(), valida con validar_email().
# Imprime con formato:
# "✅ VÁLIDO: '[email_sucio]' → '[email_limpio]'"
# "❌ INVÁLIDO: '[email_sucio]' → '[email_limpio]'"
for email_sucio in emails_test:
  email_limpio = limpiar_email(email_sucio)

  if validar_email(email_limpio):
    print(f"✅ VÁLIDO: '{email_sucio}' → '{email_limpio}'")
  else:
    print(f"❌ INVÁLIDO: '{email_sucio}' → '{email_limpio}'")