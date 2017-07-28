########################
#Funciones de alto orden
########################

############
#Funcion map
############

items=list(range(1,12))
print("Lista: ",items)

cuadrados=[]

def cuadrado(x):
	return x**2

cuadrados=list(map(cuadrado,items))

print("Lista al cuadrado: ",cuadrados)

cubos=list(map(lambda x:x**3,items))
print("Lista al cubo: ",cubos)

#######
#Filter
#######

multiplos4=list(filter(lambda n:n%3==0 and n%2==0,items))
print(multiplos4)

#######
#Reduce
#######
import functools
res=reduce(lambda a,b:a+b,items)
print(res)

#######
#Lambda
#######

#lambda parametros:Funciones
#def f(a,b):
#	return a+b

f=lambda a,b:a+b
print("Resultado", f(1,1))