#*-* coding: utf-8 *-*

import sqlite3, datetime #importamos la libreria

#conectamos a la base de datos
conexion=sqlite3.connect("chelas.sqlite")

#Seleccionamos el cursor para realizar la consulta
consulta=conexion.cursor()

#Definimos nuestra consulta
sql = "DELETE FROM bebidas WHERE id_bebida=%s" %8

#Ejecutamos la consulta
if(consulta.execute(sql)):
	print("El registro ha sido eliminado con éxito :)")
else:
	print("Error al hacer la eliminación del registro :(")

#Terminamos la consulta
consulta.close()
#Guardamos los cambios en la base de datos
conexion.commit()
#Cerramos la conexión a la base de datos
conexion.close()