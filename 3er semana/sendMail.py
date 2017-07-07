#Simple Mail Transfer Protocol
import smtplib

#Esto es muy importante porque son los datos del que envía
elQueEnvia='cursopython.proteco@gmail.com'
contra='python.isCool'

#El que recibe
elQueRecibe='diegogo.hdez@gmail.com'

#El mensaje
mensaje="""From cursoPython <cursopython.proteco@gmail.com>
To: <diegogo.hdez@gmail.com>
MIME-Version: 1.0
Content-type: text/html

Subject: Hola amigos de Avanzado

<div style="font-family: 'Pacifico', cursive; background: #CBAEAE">
<center>
<h1> Esto es el curso de <span style='color: red'> Python Avanzado</span></h1>
<p style="color: grey">El correo fue enviado desde sala B </p>
</center>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</div>
"""

try:
	smtpObjeto=smtplib.SMTP("smtp.gmail.com",587)
	smtpObjeto.ehlo() #Saludado con el método ehlo
	smtpObjeto.starttls()
	smtpObjeto.ehlo #Esto es elatributo ehlo

	#Haciendo el login con los datos del usuario que ingresamos
	smtpObjeto.login(elQueEnvia,contra)
	smtpObjeto.sendmail(elQueEnvia,elQueRecibe,mensaje)
	print("\n\n\t\tSe ha enviado tu correo! :)")
except Exception as e:
	print("ERROR, no se pudo enviar el mensaje :(")
	print(e)