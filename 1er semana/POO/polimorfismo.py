class Animal:
	def __init__(self,nombre):
		self.nombre=nombre

	#Método abstracto=el comportamiento 
	#de este método no está definido
	def hablar(self):
		raise NotImplementedError

class Perro(Animal):
	def hablar(self):
		return "Guau!"

class Gato(Animal):
	def hablar(self):
		return "Miau!"

animales=[Gato("Gatosan"),
			Perro("Max"),
			Gato("Bigotes")]

a=Animal("fantasma")
a.hablar()

for animal in animales:
	print(animal.nombre+" dice "+animal.hablar())