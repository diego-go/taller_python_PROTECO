#Así declaramos una excepción propia
class Miexcepcion(Exception):
	pass

try:
	x=1.7172
	if isinstance(x,float):
		#raise va a obligar a que ocurra una excepción
		raise Miexcepcion
except Miexcepcion:
	print("No es un entero")