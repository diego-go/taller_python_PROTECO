###################################
#El bot repite todolo que le mandes
###################################

import telebot

TOKEN='382089100:AAGC3HwUJtch4sOdmgkqM8c3dicYWP4uOCY'
chat_id=275666200

diegoMACbot=telebot.TeleBot(TOKEN)

def listener(mensajes):
	for m in mensajes:
		chat_id=m.chat.id
		if m.content_type=='text':
			text=m.text
			diegoMACbot.send_message(chat_id,"Qué pasó perro!")
			diegoMACbot.send_message(chat_id,text)

diegoMACbot.set_update_listener(listener)

diegoMACbot.polling()