import tweepy,time
from llaves import *

def conexion(tokens):
	"""Crea un objeto api para autenticar con Twitter"""
	auth = tweepy.OAuthHandler(tokens["consumer_key"],tokens["consumer_secret"])
	auth.set_access_token(tokens["access_token"],tokens["access_token_secret"])
	return tweepy.API(auth)

if __name__ == '__main__':
	bot=conexion(tokens)
	secs=4

	tweetlist=["send from #python"]
	for tweet in tweetlist:
		print(tweet)

		try:
			bot.update_status(tweet)
			print("Exitoso :D")
		except tweepy.TweepError as e:
			print(e.reason)
		time.sleep(secs)