import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
"""t=np.arange(0.0,5.0,0.2)

plt.plot(t,t,"r--",t,t**2,"bs",t,t**3,"g^") #Linea aul

plt.show()"""

#INTEGRAL DEFINIDA

def func(x):
	return (x-3)*(x-5)*(x-7)+85

a,b=2,9

x=np.linspace(0,10)
y=func(x)

#Figura y los ejes
fig,ax=plt.subplots()
plt.plot(x,y,"r",linewidth=2)
plt.ylim(ymin=0)

ix=np.linspace(a,b)
iy=func(ix)
#Dibujamos el poligono
vertices=[(a,0)]+list(zip(ix,iy))+[(b,0)]
poligono=Polygon(vertices,facecolor="0.9",edgecolor="0.5")
#Agregamos el poligono al grafico
ax.add_patch(poligono)
#Agregamos texto I f(x)dx
plt.text(0.5*(a+b),30,r"$\int_a^b f(x)\mathrm{d}x$",
	horizontalalignment="center",fontsize=20)
#Textos para los ejes
plt.figtext(0.9,0.05,"$x$")
plt.figtext(0.1,0.9,"$y$")
#Hacer invisibles las marcas en los ejes
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position("bottom")
#Poner texto en las marcas del eje x
ax.set_xticks((a,b))
ax.set_xticklabels(("$a$","$b$"))
ax.set_xticks([])

plt.show()