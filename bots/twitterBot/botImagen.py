import tweepy
from llaves import *
from io import BytexIO
import requests
from PIL import Imagen
from PIL import ImageFile

auth = tweepy.OAuthHandler(tokens["consumer_key"],tokens["consumer_secret"])
auth.set_access_token(tokens["access_token"],tokens["access_token_secret"])
api=tweepy.API(auth)

def imagenNueva(url,username,status_id):
	file='temp.png'
	request=request.get(url,stream=True)
	if request.status_code == 200:
		#Leer la imagen para descargarla en bytes y la retornamos a PIL
		i=Imagen.open(BytesIO(request.content))
		i.save(filename)
		cuadros(filename)
		api.update_with_media('nueva.png',status='@{0}'.format(username),in_reply_to_status_id=)
	else:
		print("No se pudo descargar la imagen :(")




#clase inherente a tweepy

class BotStreamer(tweepy.Strea-mListener):
	def on_status(self,status):
		username=status.user.screen_name
		status_id=status.status_id

		if 'media' in status.entities:
			for imagen in status.entities['media']:
				imagenNueva(imagen['media_url'],username,status_id)

miBot=BotStreamer()
stream=tweepy.stream(auth,miBot)
stream.filter(track=['@cornfleis'])