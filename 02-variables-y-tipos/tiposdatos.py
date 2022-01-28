#tipos de datos
nada = None
cadena_string = "Hola soy Alba Reina"
numero_entero = 25
numero_flotante = 22.5
boolean = True 
lista = [5, 10, 15, 20]
listaMixta = [5, "cinco", 10.4, "diez"] 
tuplaNoCambia = ("Master", "en", "Python")
diccionario = {
    "nombre": "Alba Maria",
    "Apellidos": "Reina Sanchez",
    "Profesion": "Odontologa"
}
rango = range(20)
dato_byte = b"prueba byte"

#imprimir variable
print(dato_byte)

#imprimir el tipo de variable
print(type(dato_byte))

#convertir datos
texto = "Hola soy un texto"
numero = 1557
numero = str(1557)

print(texto + " " + numero)

numero = float(1557)
print(type(numero))

numero = int(1557)
print(type(numero))
