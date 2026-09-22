# para QA DESTRUCTIVO

# DEFINITION OF DONE — sistema_autenticacion.py (PARA QUE UN PROGRAMA SEA ACEPTABLE► METODOLOGIAS AGILE► SCRUM► QUE UTILZA EL TESTER)

# Variables de entrada obligatorias:
#   · usuario      (str)
#   · contrasena   (str)
#   · ip_origen    (str — formato "x.x.x.x")

# Roles y comportamiento requerido:
#   superadmin:  verifica contraseña AND ip_origen.startswith("192.168.") (MÉTODO ► startswith)
#                Si ambas OK → "ACCESO TOTAL — superadmin: todos los módulos habilitados."
#                Si solo falla contraseña → "DENEGADO — superadmin: contraseña incorrecta."
#                Si solo falla IP → "DENEGADO — superadmin: acceso remoto no permitido."
#   admin:        verifica contraseña (Admin#2024)
#                OK → "ACCESO CONCEDIDO — admin: módulos de gestión habilitados."
#                Falla → "DENEGADO — admin: contraseña incorrecta."
#   auditor:      sin verificación de contraseña — acceso de solo lectura directo
#                → "ACCESO LECTURA — auditor: modo consulta activado. Sesión registrada."
#   operador:     verifica contraseña (Oper@2024)
#                OK → "ACCESO CONCEDIDO — operador: módulos operativos habilitados."
#                Falla → "DENEGADO — operador: contraseña incorrecta."
#   cualquier otro → "DENEGADO — usuario [X] no encontrado en el directorio."

# Criterios de verificación del DoD:
# → ¿El superadmin tiene un if anidado dentro de su bloque?
# → ¿El mensaje de error distingue "contraseña incorrecta" de "acceso remoto no permitido"?
# → ¿El auditor entra sin ninguna verificación de contraseña?
# → ¿El else final incluye el nombre del usuario en el mensaje? (que se imprima pues)

# -----------------------------------
# ARBOL DE DECISIONES (de lo que vamos a evaluar)
# usuario + contrasena + ip_origen
# │
# ├─ if usuario == "superadmin"
# │  ├─ red_corporativa = ip_origen.startswith("192.168.")
# │  ├─ if contrasena == "S@perAdmin2024" and red_corporativa
# │  │  └─ "ACCESO TOTAL"
# │  ├─ elif contrasena != "S@perAdmin2024"
# │  │  └─ "DENEGADO: contraseña incorrecta"
# │  └─ else
# │     └─ "DENEGADO: acceso remoto no permitido"
# │
# ├─ elif usuario == "admin"
# │  ├─ if contrasena == "Admin#2024"
# │  │  └─ "ACCESO CONCEDIDO"
# │  └─ else
# │     └─ "DENEGADO: contraseña incorrecta"
# │
# ├─ elif usuario == "auditor"
# │  └─ "ACCESO LECTURA" (sin verificar contraseña)
# │
# ├─ elif usuario == "operador"
# │  ├─ if contrasena == "Oper@2024"
# │  │  └─ "ACCESO CONCEDIDO"
# │  └─ else
# │     └─ "DENEGADO: contraseña incorrecta"
# │
# └─ else
#    └─ "DENEGADO: usuario no encontrado"


#-----------------------------------
# ejemplo breve
# nombre ="Arturo"
# if nombre.startswith("Art"):
#     print("familia Art")
#-----------------------------------

# qué hay que hacer?? agregar los IFs que faltan
# el resultado guardarlo en una variable para poder imprimir

usuario = input("nombre de usuario: ")
constrasena = input("contraseña: ")
ip_origen = input("ip origen en formato xxx.xxx.x.x: ")
red_corporativa = (ip_origen.startswith("192.168."))



 if usuario == "superadmin"
# │  ├─ red_corporativa = ip_origen.startswith("192.168.")
# │  ├─ if contrasena == "S@perAdmin2024" and red_corporativa
# │  │  └─ "ACCESO TOTAL"
# │  ├─ elif contrasena != "S@perAdmin2024"
# │  │  └─ "DENEGADO: contraseña incorrecta"
# │  └─ else
# │     └─ "DENEGADO: acceso remoto no permitido"
# │
# ├─ elif usuario == "admin"
# │  ├─ if contrasena == "Admin#2024"
# │  │  └─ "ACCESO CONCEDIDO"
# │  └─ else
# │     └─ "DENEGADO: contraseña incorrecta"
# │
# ├─ elif usuario == "auditor"
# │  └─ "ACCESO LECTURA" (sin verificar contraseña)
# │
# ├─ elif usuario == "operador"
# │  ├─ if contrasena == "Oper@2024"
# │  │  └─ "ACCESO CONCEDIDO"
# │  └─ else
# │     └─ "DENEGADO: contraseña incorrecta"
# │
# └─ else
#    └─ "DENEGADO: usuario no encontrado"