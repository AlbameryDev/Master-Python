#Formas de agregar comillas
mi_texto = '"Master"'
mi_texto2 = "\'En Python\'"

#concatenación
texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

#Salto de linea
texto_unido = mi_texto + " \n" + mi_texto2
print(texto_unido)

#Tabulacion
texto_unido = mi_texto + "\t" + mi_texto2
print(texto_unido)

#Borra todo lo que hay detrás de \r
texto_unido = mi_texto + " \r" + mi_texto2
print(texto_unido)