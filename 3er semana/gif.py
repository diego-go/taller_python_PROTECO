from tkinter import *
import time
import os
root = Tk()
# Con esta linea calcular cuantos frames tiene el gif
#frames = [print(PhotoImage(file='catslap2.gif',format = 'gif -index %i' %(i))) for i in range(200)]
#maxframes=111
#Entre más frames más tarda en cargar el gif
frames = [PhotoImage(file='catslap2.gif',format = 'gif -index %i' %(i)) for i in range(111)]

def update(ind):
	if ind==110:
		ind=0
	frame = frames[ind]
	ind += 1
	label.configure(image=frame)
	root.after(100, update, ind)

label = Label(root)
label.pack()
root.title("Ejemplo gif")
root.after(0, update, 0)
root.mainloop()