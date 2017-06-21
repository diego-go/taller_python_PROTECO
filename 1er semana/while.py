a=0
#b=3
b=int(input("Ingresa el numero que saber su tabla de multiplicar: "))


while a<=10:
	print(("%d * %d = %d")%(a,b,a*b))
	a+=1
print("Se terminó el ciclo")

a=0
while a<10:
	a+=1
	if a==2: #Se salta la iteracion del numero 2
		continue
	elif a == 5:#Ya no llegó al 5, se quedó en el 4
		break
	print(a)
print("Se terminó el segundo ciclo")

###Do while
a=0

while True:
	print("Esto se impre una vez")
	a=str(input("Salir?"))
	if a == "si":
		break
print("Se termino")