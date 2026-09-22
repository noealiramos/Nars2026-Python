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
    
else
    categoria = "nivel d"
    bono = salario *0.10
    
    print(f"categoria: {categoria}")
print(f"bono mensual: ${bono:,.2f}")
               
               