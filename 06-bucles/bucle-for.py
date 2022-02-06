"""

#FOR

for variable in elemento_iterable (lista, rango, etc...)
                BLOQUE DE INSTRUCCIONES

BREAK 
! para salir del bucle

"""

contador = 0
resultado = 0

for contador in range(0, 10):
        print ("Voy por el "+str(contador))
        
        resultado = resultado + contador
print(f"El resultado es: {resultado}")



#Ejemplo tablas de multiplicar
print("\n############# EJEMPLO ##########3")

numero_usuario = int(input("¿De que número quieres la tabla?:"))
valor = range(1,11)

if numero_usuario <1:
        numero_usuario = 1
print(f"#### Tabla de multiplicar del número {numero_usuario}")

for numero_tabla in valor:

        print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
        print("Tabla finalizada.")
