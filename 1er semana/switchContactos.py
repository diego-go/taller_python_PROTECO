#-*-coding:utf-8-*-
import os

os.system("clear")

#DICCIONARIO VACIO PARA GUARDAR CONTACTOS
contactos={}

print("\n\n\t\t\t\t\t\tBienvenido")

while True:
	print("Selecciona la opcion que deseas realizar: ")
	print("\n\t1.- Agregar un contacto.")
	print("\n\t2.- Buscar un número.")
	print("\n\t3.- Ver todos los contactos.")
	print("\n\t4.- Eliminar contacto.")
	print("\n\t5.- Salir.")

	opcionMenu=int(input("Opcion: "))
	if opcionMenu == 1:
		#Agregar contacto
		nombre = input("\n\n\tIngresa nombre del contacto: ")
		numero = int(input("\n\n\tIngresa número de teléfono: "))
		contactos[nombre]=numero
		os.system("clear")
	elif opcionMenu == 2:
		#Buscar un numero
		nombre=input("¿Qué contacto deseas buscar?")
		os.system("clear")
		if nombre in contactos:
			print("\nNombre: ",nombre)
			print("\nTelefono: ",contactos[nombre])
		else:
			print("\nContacto no encontrado")
	elif opcionMenu == 3:
		#Mostrar todos los contactos	
		os.system("clear")
		if len(contactos.items())== 0:
			print("\n\n\tNo hay contactos para mostrar")
		else:
			for persona in contactos.keys():
				print("\n\n\tEl numero de", persona, "es",contactos[persona])
	elif opcionMenu == 4:
		#Eliminar contacto
		nombre=input("¿Qué contacto deseas borrar?")
		os.system("clear")
		if nombre in contactos:
			del contactos[nombre]
		else:
			print("\n\n\tContacto no encontrado")
	elif opcionMenu == 5:
		#Para salir
		os.system("clear")
		print("\n\n\tAdios")
		break
	else:
		os.system("clear")
		print("\n\n\tOpcion inválida")