#-*-coding:utf-8-*-
import os

def numeros():
	while True:
		os.system("clear")
		print("\nSelecciona la opcion que deseas realizar: ")
		print("\n\t1.- Ver divisores de 7 y multiplos de 5")
		print("\n\t2.- Para regresar al menu")
		break
	lista1=[]
	opcion=int(input("\nOpcion: "))
	if opcion==1:
		for i in range(1500,2700):
			if i%7==0 and i%5==0:
				lista1.append(i)
		print("\n")
		print(lista1)
	elif opcion==2:
		menu()

def grados():
	while True:
		os.system("clear")
		print("\nSelecciona la opcion que deseas realizar: ")
		print("\n\t1.- Fahrenheit a Celsius.")
		print("\n\t2.- Celsius a Fahrenheit.")
		print("\n\t3.- Tipos de dato")
		print("\n\t3.- Regresar al menu principal.")
		opcionMenu=int(input("\nOpcion: "))
		if opcionMenu == 1:
		#A Celsius
			fahrenheit = int(input("\n\n\tIngresa la temperatura en grados Fahrenheit: "))
			celsius=int(((fahrenheit-32)/9)*5)
			print(fahrenheit,"°F es",celsius," grados en Celsius")
		elif opcionMenu == 2:
		#A Farenheit
			celsius = int(input("\n\n\tIngresa la temperatura en grados Celsius: "))
			fahrenheit=int(((celsius/5)*9)+32)
			print(celsius,"°C es",fahrenheit,"grados en Farenheit")
		elif opcionMenu == 3:
			menu()
		else:
			os.system("clear")
			print("\n\n\tOpcion inválida")

def menu():
	while True:
		os.system("clear")
		print("\n\n\t\t\t***BIENVENIDO***")
		print("\nSelecciona la opcion que deseas realizar: ")
		print("\n\t1.- Divisores de 7 y multiplos de 5 entre 1500 y 2700.")
		print("\n\t2.- Conversor de grados Celsius a Farenheit.")
		print("\n\t3.- Salir.")
		opcionMenu=int(input("Opcion: "))
		if opcionMenu == 1:
			numeros()
			input("\nPresiona una tecla para continuar...")
			os.system("clear")
			menu()
		elif opcionMenu == 2:
			os.system("clear")
			grados()
			break
		elif opcionMenu == 3:
			os.system("clear")
			print("\n\n\tAdios")
			break
		else:
			os.system("clear")
			print("\n\n\tOpcion inválida")

menu()