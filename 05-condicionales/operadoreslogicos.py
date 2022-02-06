"""
#Operadores Lógicos

and Y
or O
! Negacion
not No

"""

#EJEMPLO 1
print("******** EJEMPLO 1**********")

edad_paciente = int(input("¿Que edad tiene el paciente?:"))
edad_bebe = 3
edad_minima = 15

if edad_paciente <= edad_bebe and edad_paciente >= edad_minima:
    print("lo atiende Carlos")
else:
    print("lo puede atender otro doctor")


#EJEMPLO 2
print("******** EJEMPLO 2 **********")

pais = "España"

if pais == "México" or pais == "Colombia" or pais == "España" :
    print(f"{pais} Es un país de habla hispana :) !")
else:
    print(f"{pais} No es un país de habla hispana :( !")


#EJEMPLO 3
print("******** EJEMPLO 3 **********")

pais = "Alemania"

if not (pais == "México" or pais == "Colombia" or pais == "España") :
    print(f"{pais} NO un país de habla hispana :) !")
else:
    print(f"{pais} SI es un país de habla hispana :( !")
