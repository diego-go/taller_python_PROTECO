#######
#Tuplas
#######

tupla=("hola",4,10.4,True)
tupla2=("a",10,[1,2,3])
tuplaVacia=()
singleton=(1,)

print("Tipo de datos: ", type(tupla))
print("Indexación: ", tupla[0])
print("Longitud tupla: ", len(tupla))
print("Concatenacion: ", tupla+tupla2)
print("Longitud 2 tuplas: ", len(tupla+tupla2))

#No se permite porque la tupla es inmutable
#tupla[0]="HOLA"

tupla2[2][1]=0
print(tupla2)