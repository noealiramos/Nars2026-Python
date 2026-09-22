# Código plano — sistema de monitoreo de SLA
#reglas de neogcio tres niveles

# El código es de un sistema de monitoreo de SLAs de atención a clientes

# Los 4 caminos que debe ejecutar correctamente:
# crítico + 10 min + cualquiera  →  "SLA CUMPLIDO: Respuesta crítica..."
# crítico + 25 min + si          →  "VIOLACIÓN SLA: Cliente premium — escalar..."
# crítico + 25 min + no          →  "VIOLACIÓN SLA: Notificar cliente..."
# alto + 90 min + cualquiera     →  "VIOLACIÓN SLA: Alta prioridad — notificar supervisor"
# medio + cualquier cosa          →  "SLA estándar: Prioridad media..."

#codigo original►1♠
# Código plano — sistema de monitoreo de SLA
# tipo_incidente = input("Tipo de incidente (critico/alto/medio): ")
# tiempo_respuesta = int(input("Tiempo de respuesta (minutos): "))
# cliente_premium = input("¿Cliente premium? (si/no): ")
# if tipo_incidente == "critico":
# if tiempo_respuesta <= 15:
# print("SLA CUMPLIDO: Respuesta crítica dentro del límite.")
# else:
# if cliente_premium == "si":
# print("VIOLACIÓN SLA: Cliente premium — escalar a dirección.")
# else:
# print("VIOLACIÓN SLA: Notificar cliente y registrar penalización.")
# elif tipo_incidente == "alto":
# if tiempo_respuesta <= 60:
# print("SLA CUMPLIDO: Alta prioridad dentro del límite.")
# else:
# print("VIOLACIÓN SLA: Alta prioridad — notificar supervisor.")
# else:
# print("SLA estándar: Prioridad media — manejo rutinario.")


#RESPUESTA►►►

tipo_incidente = input("Tipo de incidente (critico/alto/medio): ")
tiempo_respuesta = int(input("Tiempo de respuesta (minutos): "))
cliente_premium = input("¿Cliente premium? (si/no): ")


if tipo_incidente == "critico":
    if tiempo_respuesta <= 15:
        print("SLA CUMPLIDO: Respuesta crítica dentro del límite.")
    else:
        if cliente_premium == "si":
            print("VIOLACIÓN SLA: Cliente premium — escalar a dirección.")
        else:
            print("VIOLACIÓN SLA: Notificar cliente y registrar penalización.")

elif tipo_incidente == "alto":
    if tiempo_respuesta <= 60:
        print("SLA CUMPLIDO: Alta prioridad dentro del límite.")
    else:
        print("VIOLACIÓN SLA: Alta prioridad — notificar supervisor.")

else:
    print("SLA estándar: Prioridad media — manejo rutinario.")