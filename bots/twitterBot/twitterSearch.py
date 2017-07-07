from TwitterSearch import *

try:
	tso=TwitterSearchOrder()
	tso.set_keywords(["México","Alemania"])
	tso.set_language("es")
	tso.set_include_entities(False)

	ts=TwitterSearch(
		consumer_key="chM8hRtw4oHi68vYZDWZmOTIv",
		consumer_secret="5BP9xEHMs4d0lwVRRROjj3uc6584DGQf69ahkYevivC1jlS1Pc",
		access_token="94164223-RIxNCQS7u3E1zo4hz5wCnv1h91y9idM8g6ztNfvWE",
		access_token_secret="yRguFKCaS29X7F2fqPuroHktwXYc2YtK28D9poDz58w6s"
	)

	for tweet in ts.search_tweets_iterable(tso):
		print("@%s twitteo: %s"%(tweet["user"]["screen_name"],tweet["text"]))
except TwitterSearchException as tse:
	print("Hubo un error: ",tse)