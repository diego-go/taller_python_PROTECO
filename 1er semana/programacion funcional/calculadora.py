##########
#Funciones
##########
import math

print(eval(input))

def suma(a,b):
	print("suma")
	print(a, "+", b)
	return a+b

def resta(a,b):
	print("\nresta")
	print(a,"-",b)
	return a-b

def multiplicacion(a,b):
	print("\nmultiplicacion")
	print(a,"x",b)
	return a*b

def division (a,b):
	print("\ndivision")
	print(a,"/",b)
	return a/b

def raiz(a):
	print("\nraiz")
	print("sqrt",a)
	return math.sqrt(a)

def potencia(a):
	print("\npotencia")
	print(a,"^3")
	return pow(a,3)

a, b = 4, 10
print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,b))
print(raiz(a))
print(potencia(a))