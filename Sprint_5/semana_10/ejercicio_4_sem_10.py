nombre_sucio = " ana   torres "
eamil_sucio = " ANA.Torres@Inadaptados.MX"
area_sucia= "finazas"
habilidades_raw = "Python, sql, Excel, power bi"

nombre = nombre_sucio.strip()
print(f"[{nombre}]") # los corchetes nos dejan ver los espacios
      
nombre = nombre.replace("   "," ")
nombre = nombre.title() #pone en mayuscula la primera letra de cada palabra
print(f"[{nombre}]") # los corchetes nos dejan ver los espacios