#################
#Imagenes tkinter
#################

from tkinter import *

ventana=Tk()
ventana.title("Imagen")

logo=PhotoImage(file="py2.png")
label1=Label(ventana,image=logo).pack(side="right")
text="""Para utilizar imagenes con python, se deben
utilizar los formatos PNG o GIF, o utilizar el modulo
PIL para otros formatos.
"""

label2=Label(ventana,justify=LEFT,padx=10,text=text).pack(side="left")
ventana.mainloop()