"""
#Condicional IF


SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de instrucciones

If condicion:
    instrucciones
Else:
    otras instrucciones


#Operadores de comparacion
== igual 
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que



"""


# EJEMPLO 1
print("\n******************** EJEMPLO 1 *******************")

#color = "Rosa"
color = input ("¿Cual es mi color favorito?:")

if color == "azul":
    print("Muy bien")
    print("El color es azul")
else:
    print("Fallaste, el color no es ese")


#EJEMPLO 2
print("\n******************* EJEMPLO 2******************")

#Year = 2022
year = int(input("¿En que año estamos?:"))

if year == 2022:
    print("Bien, estamos en el año 2022!")

else: 
    print("No estamos en ese año")


#EJEMPLO 3

print("\n**********************EJEMPLO 3************************")


nombre = "Alba María"
ciudad = "Málaga"
pais = "España"
profesion = "Auxiliar de odontología e Higienista Dental"
edad = 25
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    estudios = input("¿Has estudiado una carrera?")
    if estudios == "si":
        print("Enhorabuena, estás preparado.")
    else:
        print ("No tienes estudios suficientes")

else:
    print(f"{nombre} No es mayor de edad")

