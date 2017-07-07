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