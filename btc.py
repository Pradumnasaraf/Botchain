import tweepy
import time
import json
import requests

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
Ticker =1
while True:

    try:
        # Using get api method getting lastest price of bitcoin in USD
        BitCoin = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        
        # callling json() on the string.
        price = BitCoin.json()

        # Getting the value by using keys
        Coin = price['bitcoin']['usd']

        # Meassge that will include in the tweet
        FinalMessage = 'Current #Bitcoin Price is '+ str(Coin)+'$ #BTC #Crypto'

        # update_status let us to post tweet having some kind of content
        api.update_status(FinalMessage)

        #Added Ticket to keep track of no of tweet bot has tweeted.
        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1

        # Bot sleeping 5 min after Every tweet
        time.sleep(300)

    # Hadling Any kind of errors like (Responce error, Simliar tweet)
    except tweepy.TweepError as e:
        print(e.reason)

        #Printing the error message
        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1
        time.sleep(300)
