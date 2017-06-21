#*-* coding: utf-8 *-*

import sqlite3, datetime #importamos la libreria

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()

sql="select * from bebidas"

if(consulta.execute(sql)):
	filas=consulta.fetchall()
	for fila in filas:
		print(fila[0],fila[1],fila[2],fila[3])

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()