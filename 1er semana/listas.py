########
#CADENAS
########

lista=["hola",4,10.4,True]
lista2=["a",10,[1,2,3]]
listaVacia=[]

print("Tipo de datos: ", type(lista))
print("Indexación: ", lista[0])
print("Longitud lista: ", len(lista))
print("Concatenacion: ", lista+lista2)
print("Longitud 2 listas: ", len(lista+lista2))
#LAS LISTAS SÍ SON MUTABLES
lista[0]="HOLA"
print(lista[0])
print("Búsqueda: ", 10.4 in lista)

print("\n")
#sublista
print("Elementos en sublista ", lista2[2][1])

for elemento in lista:
	print("Elemento: ",elemento)

print("Slicing:", lista[1:3])
print("Slicing: ",lista[: :-1])

#Operaciones
lista=["A","B","C","D"]
lista.append("E")#Añade un elemento a una lista
print(lista)

#POSICIÓN
lista.insert(0,"Z")
print(lista)

ultimoElemento=lista.pop()
print(ultimoElemento)
print(lista)

#Eliminacion del elemento
print("Eliminacion del elemento")
del lista[0]
print(lista)

lista2=[2,3,1,5,8,2]
print("Maximo: ",max(lista2))
print("Minimo: ",min(lista2))

#Sort ordena de menor a mayor
lista2.sort()
print("Lista ordenada: ", lista2)

lista2.reverse()
print("Lista ordenada inverso: ", lista2)

#Indice de un elemento
print("Indice de B: ", lista.index("B"))

