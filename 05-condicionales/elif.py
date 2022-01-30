# EJEMPLO 
print ("********************EJEMPLO*******************")

dia = int(input("¿Que numero de día de la semana es?:"))

# SI es igual a 4 
#dile que es jueves

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado y es fin de semana")
elif dia == 7:
    print("Es domingo y es fin de semana")
else:
    print("Día no válido")
