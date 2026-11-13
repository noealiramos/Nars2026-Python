# Caso 1: Normalizar Nombre de Usuario
# Problema: El usuario escribe su nombre de cualquier forma.
# Objetivo: Formato consistente - "Nombre Apellido" (cada palabra con mayúscula inicial).

print("=== NORMALIZACIÓN DE NOMBRES ===\n")

nombres_sucios = [
  "  JUAN PÉREZ  ",
  "ana maría lópez",
  "CARLOS   RUIZ",
  "  María   "
]

print("--- NOMBRES SUCIOS ---")
for nombre in nombres_sucios:
  print(f"'{nombre}'")

print("\n--- NOMBRES LIMPIOS ---")
for nombre_sucio in nombres_sucios:
  # Encadenamos: quitar espacios externos -> minúsculas -> mayúscula inicial
  nombre_limpio = nombre_sucio.strip().lower().title()
  print(f"'{nombre_limpio}'")

# Espacios dobles internos
nombre_usuario = "  JUAN   PÉREZ  "
nombre_final = nombre_usuario.strip().title()

if "  " in nombre_final:
  # split() sin argumentos separa por cualquier cantidad de espacios
  nombre_final = " ".join(nombre_final.split())

print(f"\nNombre guardado en BD: '{nombre_final}'")
