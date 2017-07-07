#######
# Numpy
#######

import numpy as np

a=np.array([1,2,3])
print("Tipo de dato: ",type(a))
print("Dimension: ",a.shape)
print("Indexacion: ",a[0],a[1],a[2])
#Asignación por item
a[0]=5
print("Dato: ",a[0])
print("Imprimir el array ",a)

b=np.array([[1,2,3],[4,5,6]])
print("Tipo de dato: ",type(b))
print("Dimension: ",b.shape)
print("Indexacion: ",b[0,0],b[0,1],b[1,0]) #1 2 4

#Funciones para generar espacios de numeros

a=np.arange(10) #0...9 no es inclusivo
print(a)
b=np.arange(0,11,2) #0...11 de dos en dos
print(b)

#linspace

c=np.linspace(0,1,6) #inicio,fin,numero de puntos que queremos
print(c) #Es inclusivo

d=np.linspace(0,1,6,endpoint=False) #inicio,fin,numero de puntos que queremos
print(d) #No es inclusivo

e=np.linspace(0,1,101)
print(e)

#Funciones para crear matrices

a=np.zeros((2,2))
print(a)

b=np.ones((2,2)) #Inicializado con unos
print(b)

e=np.full((2,2),7) #Inicializado con una constante
print(e)

f=np.eye(3)
print("Matriz identidad\n",f)

g=np.random.random((2,2))
print("Aleatorio\n",g)

print("\n")
#Matriz del 1 al 12 que tenga la forma (3,4) matriz 3x4

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
#Slicing en nd arrays es así

b=a[:2,1:3]
print(b)

print("-> ",a[0,1]) #Numero 2
b[0,0]=77
print(a[0,1])

#Tipos de datos numéricos
x=np.array([1,2])
print(x.dtype)

y=np.array([1.0,2.0])
print(y.dtype)



#Operaciones con matrices
import numpy as np

x=np.array([[1,2],
			[3,4]], 
			dtype=np.float64)
y=np.array([[5,6],
			[7,8]], 
			dtype=np.float64)

#Elemento elemento
print("Suma: \n",x+y)
print("Resta: \n",np.subtract(x,y))

print("Multiplicacion: \n",x*y)
print("Division\n",x/y)
print("Raiz:\n",np.sqrt(x))

#Multiplicacion de matrices
v=np.array([9,10])
w=np.array([11,12])

#Producto punto
print("Producto punto\n",v.dot(w))

print(x.dot(v))

#Producto matricial
print(np.dot(x,v))

#x * y
print("x*y:\n",x.dot(y))

print("x*I\n",x.dot(np.eye(2)))

#x^-1 inversa

inversaX=np.linalg.inv(x)
print("Inversa\n",inversaX)

print("x*x⁻¹\n",x.dot(inversaX))

determinante=np.linealg.determinante(x)
print("Determinante\n", determinante)