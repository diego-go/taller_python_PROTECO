class A:
	def a(self):
		print("A")

class B(A):
	def a(self):
		print("B")

class C(A):
	def a(self):
		print("C")

class D(C,B):
	def preguntaPorA(self):
		self.a()

objetoD=D()
objetoD.preguntaPorA()

print(D.__mro__)