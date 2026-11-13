bono_local = 2000

def procesar():
    global bono_local
    bono_local += 500
    print("Bono local actualizado:", bono_local)    
    
    procesar
    