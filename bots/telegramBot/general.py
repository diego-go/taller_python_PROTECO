#######################
#API Telegram para bots
#######################

import telebot

TOKEN='382089100:AAGC3HwUJtch4sOdmgkqM8c3dicYWP4uOCY'

#Creamos objeto de la clase telebot con el método TeleBot() le pasamos el token

#Nombre del bot  #Instancia del bot
diegoPythonbot = telebot.TeleBot(TOKEN)

#Con este método vemos si funciona la API
diegoPythonbot.get_me()

print(diegoPythonbot.get_me())

#Enviar mensaje
mensaje="Hola, soy un bot"
chat_id=275666200

#while True:
diegoPythonbot.send_message(chat_id,mensaje)

#Enviar imágenes
#foto=open('cat.gif','rb')
#diegoPythonbot.send_photo(chat_id,foto)

#doc=open('docker.pdf','rb')
#diegoPythonbot.send_document(chat_id,doc)
"""
video=open('epn.mp4','rb')
diegoPythonbot.send_video(chat_id,video)"""

#audio=open('epn.mp4','rb')
#diegoPythonbot.send_audio(chat_id,audio)

#latitud = 19.331493
#longitud = -99.185065

#diegoPythonbot.send_location(chat_id,latitud,longitud)

from telebot import types

#markup=types.ReplyKeyboardMarkup(row_width=2)
#item1=types.KeyboardButton('a')
#item2=types.KeyboardButton('v')
#item3=types.KeyboardButton('d')
#markup.add(item1,item2,item3)

#diegoPythonbot.send_message(chat_id,'Elige una letra: ',reply_markup=markup)