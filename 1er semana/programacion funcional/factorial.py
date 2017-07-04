##########
#Recursion
#########

def factorial(num):
	if num<1:
		return 1
	else:
		return num*factorial(num-1)

numero=int(input("Ingresa numero: "))
print(factorial(numero))

##########
#Iteracion
##########

def factorial2(num):
	fac=1
	for i in range(2,num+1):
		fac*=i
	return fac

numero=int(input("Ingresa numero: "))
print(factorial2(numero))