colores={'rojo':'red','verde':'green','negro':'black'}
try:
	color=input("Ingresa un color: ")
	if color in colores.keys():
		print("El color está en la lista")
	else:
		print(colores[color])
except KeyError:
	print("El color no está en la lista")