from TwitterSearch import *
import matplotlib.pyplot as plt
import collections,sys,math

def FindHashHags(tweet):
    """
    Esta funcion toma como entrada un tweet ,
    se limpia el texto y el formato , y devuelve
    el conjunto de todos los hashtags en el tweet.
    """
    tweettxt = tweet['text']#.encode('ascii','ignore')
    tweettxt = tweettxt.replace('#',' #')
    for punct in '.!",;:%<>/~`()[]{}?':
        tweettxt = tweettxt.replace(punct,'')
    tweettxt = tweettxt.split()
    hashtags = []
    for word in tweettxt:
   
        if word[0]=='#':
            hashtag = word.lower()
            hashtag= hashtag.split('\'')[0]         
            hashtag = hashtag.replace('#','')
       
            if len(hashtag)>0:
                hashtags.append(hashtag)
    return hashtags

def HashSearch(hashtag):
    """
    Esta es la funcion que realiza la busqueda del hashtag,
    y encuentra todos los otros hashtags en los demas tweets.
    Regresa un histograma de la frecuencia de los otros hashtags.
    """
    hashtag = hashtag.lower()
 
    CoTags = []
    ntweets = 0
    basictag = hashtag.lower()
    basictag = basictag.replace('#','')
 
    ts = TwitterSearch(
		consumer_key="chM8hRtw4oHi68vYZDWZmOTIv",
		consumer_secret="5BP9xEHMs4d0lwVRRROjj3uc6584DGQf69ahkYevivC1jlS1Pc",
		access_token="94164223-RIxNCQS7u3E1zo4hz5wCnv1h91y9idM8g6ztNfvWE",
		access_token_secret="yRguFKCaS29X7F2fqPuroHktwXYc2YtK28D9poDz58w6s"
    )
   

    tso = TwitterSearchOrder() 
    tso.set_keywords([hashtag]) 
    tso.set_language('es')
    tso.remove_attitude_filter()
    #Descomentar si devuelve una excepcion: Request cannot be served due to the application's rate limit
    #del ts.exceptions[429]
 
    for tweet in ts.search_tweets_iterable(tso): 
        hashtags = FindHashHags(tweet)
   
        for atag in hashtags:
            if basictag not in atag:
                CoTags.append(atag)
   
        if ntweets == 1000:
            break
        ntweets += 1
 
    taghisto = collections.Counter(CoTags)
    taghisto = [list(x) for x in sorted(taghisto.items(), key=lambda x: -x[1])]
     
    ntweets = float(ntweets)
    for ibin in range(len(taghisto)):
        uncertainty = math.sqrt(taghisto[ibin][1])
        taghisto[ibin][1]= 100.*taghisto[ibin][1]/ntweets
        taghisto[ibin].append(100.*uncertainty/ntweets)
    return taghisto

def DrawHisto(taghisto,atag):
    """
    Esta funcion grafica el historiograma
    """
    N = 0
    for t in taghisto:
        if t[2]<0.3*t[1]:
            N+=1
        if N==10:
            break
    labels = ['#'+taghisto[n][0] for n in range(N)]
    content = [taghisto[n][1] for n  in range(N)]
    errors = [taghisto[n][2] for n  in range(N)]
 
    plt.barh(range(N), content,xerr=errors, align='center',alpha=0.4)
    plt.yticks(range(N), labels)
    plt.xlabel('Porcentaje de Hashtags compartidos')
    plt.title('Hashtags compartidos para #'+mytag)
    plt.xlim(0.0,max(content)*1.2)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
	mytag=input('Ingrese el hashtag a buscar (u oprima enter para ver un ejemplo): ')
	if mytag=="":
		mytag = "StarWars"
	myhisto = HashSearch('#'+mytag)
	DrawHisto(myhisto,mytag)