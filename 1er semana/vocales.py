lista=[]
vocales={}
cond=True
while(cond):
	cadena=input("Ingresa cadena: ")
	lista.append(cadena)
	cond=int(input("Ingresa 1 si quieres agregar y 0 si ya no quieres agregar: "))

print(lista)

for cadena in lista:
	vocales[cadena]=0
	for letra in cadena:
		if letra in ["a","e","i","o","u"]:
			vocales[cadena]+=1

print(vocales)