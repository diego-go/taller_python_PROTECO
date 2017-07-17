#########
#Archivos
#########

#open(rutaDelArchivo,modo) modo por default en solo lectura

archivo=open("archivo.txt",'a+')
print("Nombre del archivo: ",archivo.name)
print("Modo del archivo: ",archivo.mode)

#Siempre recordar cerrar los archivos o flujos de datos
#archivo.close()

if archivo.close:
	print("El archivo está cerrado")
else:
	print("El archivo está abierto")

#texto=archivo.read()
#print(texto)
#print(type(texto))

texto=input("Ingrese texto para eascribir en el archivo: ")
archivo.write("\n"+texto)

#Mover el apuntador
archivo.seek(0) #bytes

print("Contenido del archivo: ",archivo.read())

archivo.close()

#Manejador de contexto

with open(input("Ingrese el nombre del archivo: ")) as f:
	lineas=f.readlines()

print(lineas)

for linea in lineas:
	print(linea,end="")