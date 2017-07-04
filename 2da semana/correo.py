import re

correo=input("Ingresa tu correo: ")

#patron="\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}"
patron=('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z){2,3}$')

valido=re.match(patron,correo)
if valido:
	print("El correo es valido")
else:
	print("No es un correo valido")
