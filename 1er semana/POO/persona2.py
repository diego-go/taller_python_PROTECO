class Persona2:
	#Constructor
	def __init__(self):
		print("Se ha creado una persona, y se imprimió este mensaje")
	def saludar(self):
		print("Hola soy una persona")
	def comer(self):
		print("Estoy comiendo")
	def estudiar(self):
		print("Estoy aprendiendo POO")

juan=Persona2()
edgar=Persona2()
diego=Persona2()

juan.saludar()
edgar.comer()
diego.estudiar()