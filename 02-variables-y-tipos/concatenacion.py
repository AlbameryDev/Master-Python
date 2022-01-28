#concatenación

nombre = "Alba Maria"
apellidos = "Reina Sanchez"
profesion = "Higienista dental y auxiliar de odontologia"

# Tipo de concatenacion 1
print(nombre + " " + apellidos + " - " + profesion) 

# Tipo de concatenacion 2
print(f"{nombre} {apellidos} - {profesion}")

# Tipo de concatenacion 3
print ("Hola me llamo {} {} y trabajo como {}".format(nombre,apellidos,profesion))

# Tipo de concatenacion 4
datos = (nombre + " " + apellidos + " - " + profesion)

print(datos)
