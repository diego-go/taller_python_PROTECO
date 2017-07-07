import tweepy
import datetime
from llaves import tokens

def getAPI(tokens):
	"""Crea un objeto api para autenticar con Twitter"""
	auth = tweepy.OAuthHandler(tokens["consumer_key"],tokens["consumer_secret"])
	auth.set_access_token(tokens["access_token"],tokens["access_token_secret"])
	return tweepy.API(auth)

def conectar(tokens):
	api=getAPI(tokens)
	print("Autenticación exitosa! :)")

	fecha=datetime.date.today()
	tweet="Probando #tweepy."
	status=api.update_status(status=tweet)
	return status

if __name__=='__main__':
	conectar(tokens)