#########
#ModuloOS
#########

import os
#Conocer el nombre del sistema operativo o entorno que correo python
print("Nombre del sistema operativo: ",os.name)

#Invocar un comando externo
#os.system("lsb_release -a")

#Saber el directorio actual
print("Current directory: ",os.getcwd())

#Caracteristicas del sistem
#print(os.uname())

#Listar un directorio
print(os.listdir("."))

#os.rmdir("Nueva Carpeta")

#Crear un directorio
#os.mkdir("Nueva Carpeta")

#os.chdir("Nueva Carpeta")
print("directorio actual: ",os.getcwd())

os.rename("Nueva Carpeta","Carpeta Renombrada")
print(os.listdir("."))
