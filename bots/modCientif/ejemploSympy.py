#######
# Sympy
#######

from sympy import *
init_printing(use_unicode=False,wrap_line=False,no_global=False)

x=Symbol("x")
y=Symbol("y")
z=Symbol("z")

#e^x para x=pi

print("e^x, x=pi",exp(x).subs(x,pi).evalf)

expresion=x+2*y
print("x + 2*y ; x=1 y=2:",expresion.subs(x,1).subs(y,2))

expresion=Rational(3,2)*pi + exp(I*x) / (x**2+y)
print(expresion)

fx=x**2+x+1

print("Evaluación en un punto x=0\n",fx.subs(x,0).evalf())

#pprint(integrate(fx))

#pprint(diff(fx))

#pprint(integrate(expresion,x))

ecu=x**3+2*x**2+4*x+8
print("Raices: ",solve(Eq(ecu),x))

e1=x+5*y-2
e2=-3*x+6*y-15

print("Sistema de ecuaciones:\n",solve([e1,e2],[x,y]))

sistema=[x+5*y-2,
		-3*x+6*y-15,
		x+7*y-12*z]

print("Sistema de ecuaciones:\n",solve(sistema,[x,y,z]))