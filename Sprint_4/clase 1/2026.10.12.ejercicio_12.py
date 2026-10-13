incidentes = ["txt-101: adfadfadf", 
              "txt-102: adadfadfad", 
              "txt-103: adfadafadff",
              "txt-104:adfadsfasdafd",
              "txt-102: adadfadfad"]

incidentes.remove("txt-102: adadfadfad") #borrar el primer elemento que coincida con el valor especificado, es decir, si hay varios elementos con el mismo valor, solo se eliminará el primero que se encuentre.
print(incidentes)

print(f"{'-'* 20}") #--------------------
# incidentes.remove("txt-999") #arrojará un error, ya que el elemento "txt-999" no se encuentra en la lista.  
# print(incidentes)

