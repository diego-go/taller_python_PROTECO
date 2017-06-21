#*-* coding: utf-8 *-*

import sqlite3,datetime #importamos la libreria

#Recibimos los valores que el usuario quiere almacenar
print("*******Bienvenido*******")
nombre=input("Introduce el nombre de la bebida: ")
precio=input("Introduce el precio de la bebida: ")

try:
	precio=float(precio) or int(precio)
except ValueError:
	print(precio, "no es un numero entero o flotante")
	exit()

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()
#Almacenando los datos en una tupla
argumentos=(nombre, precio, datetime.date.today()) #yyyy-mm-dd

#Creando string con la consulta SQL
sql="""
INSERT INTO bebidas(nombre,precio,exportacion)
VALUES (?,?,?)
"""

if(consulta.execute(sql,argumentos)):
	print("Registro guardado existosamente :)")
else:
	print("Error al guardar el registro :(")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()