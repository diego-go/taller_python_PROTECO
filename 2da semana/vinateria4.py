#*-* coding: utf-8 *-*

import sqlite3, datetime #importamos la libreria

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()

#Definimos nuestra consulta
sql = "UPDATE bebidas SET nombre = \"Jack\" WHERE id_bebida=%s" %4

#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("Registro modificado con éxito :)")
else:
	print("Error al hacer la modificación :(")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()