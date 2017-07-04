##########
#Funciones
##########

def suma(a,b):
	"""Docstring"""
	return a+b

a, b = 2, 4
print(suma(a,b))
print(suma(3.4,6))
#Keyword argument
print(suma(a=10,6))

def suma2(a=1,b=3):
	return a+b

#Parametros por default
print("Parametros por default")
print(suma2())
print(suma2(a,b))

def suma3(*variables):
	acum=0
	for numero in variables:
		acum+=numero
	return acum

print("Parametros variables")
print(suma3(1,2))
print(suma3(1,2,3))
print(suma3(1,2,4,5,6))

def suma4(a=0,b=0,**llavevalor):
	if llavevalor is not None:
		for llave, valor in llavevalor.item():
			print("Llave: ",llave,"Valor: ", valor)
	else:
		return a+b

print(suma4())
print(suma4(1))
print(suma4(1,3))
print(suma4(nombre="diego"))
print(suma4(nombre="diego", apellido="hdz", semestre=5))