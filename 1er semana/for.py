##########
#Ciclo for (for in)
##########

lista=[1,2,3,4,5]

#for i in lista:
	#print(i)

#tupla=("uno",1,1.0,1+2j,[1,1,1])

#for val in tupla:
#	print(val)

#for j in range(5,0,-1):
#	print(j)

"""a=1
b=-5

if a>5 or b>0:
	print(a, b)
else:
	if a>0 and b> -10:
		print(a,b)

#Lo mismo pero más resumido
if a>5 and b>0:
	print(a,b)
elif a>0 and b> -10:
	print("Los numeros son menores ahora", a,b)

"""
for i in range(1,10):
	if i == 7:
		print("Este si",i)
		break
	else:
		print("Este no es el que buscas", i)
	print("Sigue intentando")