saldo_disponible=1000
cargo_diario = 150
dias_transcurridos = 0

while saldo_disponible > 0:
   saldo_disponible=saldo_disponible - cargo_diario
   dias_transcurridos +=1 #que es lo mismo que dias_transcurridos = dias_transcurridos+1
   print(f"dia {dias_transcurridos}: saldo = $ {saldo_disponible}")