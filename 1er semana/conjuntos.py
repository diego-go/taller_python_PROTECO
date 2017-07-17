##########
#Conjuntos
##########

conjunto={1,2,3,4,5}

print("Tipo de dato", type(conjunto))
print(conjunto)

conjunto2=set([1,2,2,3,3,4,5,6,9])
print(conjunto2)

conjunto3={True,3,40,"hola"}
print(conjunto3)
conjunto3.add(False)

#No soporta indexacion
#print("Indexación: ",conjunto[0])

print("Tamaño de conjunto: ",len(conjunto))
#NO SOPORTA CONCATENACIÓN
#print("Concatenación: ",conjunto+conjunto2)
#NO SOPORTA ESTA OPERACION
#print("Repetición: ", conjunto*3)

print("Diferencia: ",conjunto-conjunto2)
print("Diferencia simética: ", conjunto^conjunto2)
print("Union: ", conjunto|conjunto2)
print("Interseccion: ", conjunto&conjunto2)

###########
#Frozensets
###########

conjuntoF= frozenset([True,3,40,"hola"])
print(conjuntoF)
#NO PERMITIDO
conjuntoF.add(False)
print(conjuntoF)
