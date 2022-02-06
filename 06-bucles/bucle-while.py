""" 

# BUCLE WHILE
Estructura de control que itera o repite la ejecución de una serie de instrucciones 
tantas veces como sea necesario,
hasta que deje de cumplirse la condicion


While condición
    bloque de intrucciones
    actualizacion de contador

"""
### EJEMPLO 1 ###

contador = 1

while contador <=100:
    print(f"Estoy en el número {contador}")
    contador += 1


#### EJEMPLO 2###

contador = 1
muestrame =str (0)


while contador <=100:
    print(f"Estoy en el número {contador}")

    muestrame = muestrame + ", " + str(contador)
    contador += 1

    print(muestrame)
