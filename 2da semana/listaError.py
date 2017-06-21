class DentroRango(Exception):
	pass

lista=[1,2,3,4,5]

while True:
	try:
		numero=int(input("Ingresa un valor: "))
		lista[numero]
		if numero > 5:
			print("El valor está fuera de rango")
			raise IndexError
		elif numero < 5:
			print("El valor esta dentro de la lista")
			raise DentroRango
	except DentroRango:
		print("Dentro de rango")
	except IndexError:
		print("Fuera de rango")