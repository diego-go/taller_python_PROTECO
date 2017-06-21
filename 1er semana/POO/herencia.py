class Terrestre:
	def moverse(self):
		return ("Soy un "+self.__class__.__name__+" y camino en la tierra")

class Animal:
	def __init__(self,patas1,nombre1,peso1):
		self.patas=patas1
		self.nombre=nombre1
		self.energia=0
		self.peso=peso1
	def comer(self):
		self.energia+=1
		print(self.energia)
	def hablar(self):
		print("Grrrrrrr!")

#Un perro es un animal y es terrestre
class Perro(Animal,Terrestre): #Dentro de la clase, va de dónde vamos a heredar
	def __init__(self,nombre,peso):
		super().__init__(4,nombre,peso)#Manda llamar a la clase padre y obtiene los atributos
	#Se manda a llamar cuando se manda a imprimir el objeto por medio de print
	def __str__(self):
		return str("Soy un objeto")
	def hablar(self):
		print("Guau guau!")

lucho=Perro("lucho",30)
firulais=Perro("firulais",40)

lucho.hablar()
lucho.comer()

print(lucho)
print(lucho.moverse())