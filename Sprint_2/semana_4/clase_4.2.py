salario =float(input("salario mensual bruto:"))

if salario > 5000:
    categoria = "nivel a - directivo"
    bono = salario * 0.20
    
elif salario >25000:
    categoria = "nivel b - semi senior"
    bono = salario * 0.15
    
elif salario >15000:
    categoria = "nivel c - senior"
    bono = salario * 0.10
    
else:
    categoria = "nivel d"
    bono = salario *0.10
    
##print (bono) 

print(f"categoria: {categoria}")
print(f"bono mensual: ${bono:,.2f}")
               
# el sistema para que salrio >50,000 sea nive a (20%)
# salario >35,000 sea nivel b (15%)
# salario >15,000 sea nivel c (10%)
# y cualquier otro sea junio (5%)

#o pueden cambiar los numero, sólo el ordens