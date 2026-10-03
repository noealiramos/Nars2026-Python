saldo_disponible=1000
cargo_diario = 150
dias_transcurridos = 0

#while saldo_disponible > 0 and saldo_disponible>=150:
while saldo_disponible > 0:
   saldo_disponible=saldo_disponible - cargo_diario
   dias_transcurridos +=1 #que es lo mismo que dias_transcurridos = dias_transcurridos+1
   print(f"dia {dias_transcurridos}: saldo = $ {saldo_disponible}")
   
print(f"\nEl saldo se agotó despues de {dias_transcurridos} dias.")
print(f"saldo final: ${saldo_disponible}")


# Vuelta │ saldo (antes) │ saldo (después) │ dias_transcurridos │ ¿condición True?
# ───────┼───────────────┼─────────────────┼────────────────────┼─────────────────
#   1    │  1000         │  850            │  1                 │ Sí (1000 > 0)
#   2    │  850          │  700            │  2                 │ Sí (850  > 0)
#   3    │  700          │  550            │  3                 │ Sí (700  > 0)
#   ...  │  ...          │  ...            │  ...               │ ...
#   7    │  100          │  -50            │  7                 │ Sí (100  > 0)
#   8    │  -50          │  ─              │  ─                 │ No (-50 < 0) → sale