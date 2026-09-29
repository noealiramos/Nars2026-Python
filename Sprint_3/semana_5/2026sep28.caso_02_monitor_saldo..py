# "Contexto real. Trabajas en el área de crédito de un banco. 
# Te piden un script que simule lo siguiente: una cuenta empresarial 
# tiene un saldo disponible de $1,000. Cada día se le carga un cargo 
# fijo de $150 por servicios. 

# Tu programa tiene que decirme cuántos días pasan antes de que el saldo 
# llegue a cero o se quede en negativo, y cuál es el saldo final."

saldo = 1000
cargo = 150
dias = 0

while saldo >0: 
   saldo = saldo - cargo #es igual a "saldo -=cargo"
   dias = dias + 1 #es igual a "dias +=1"
   print(f"los dias de saldo son: {dias} y el saldo es: {saldo}")

print(f"los dias de saldo: {dias}")