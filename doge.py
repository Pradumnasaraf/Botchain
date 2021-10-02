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
        # Using get api method getting lastest price of doge in USD
        DogeCoin = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')

        # callling json() on the string.
        price = DogeCoin.json()

        # Getting the value by using keys
        Coin = price['dogecoin']['usd']

        # Meassge that will include in the tweet
        FinalMessage = 'Current #DOGE Price is '+ str(Coin)+'$ #Dogecoin #Crypto #ToTheMoon'

        # update_status let us to post tweet having some kind of content
        api.update_status(FinalMessage)

        #Added Ticket to keep track of no of tweet bot has tweeted.
        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1

        ##Bot sleeping for 5 min, after Every tweet
        time.sleep(300)

    # Hadling Any kind of errors like (Responce error, Simliar tweet)
    except tweepy.TweepError as e:
        print(e.reason)

        #Printing the error message
        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1
        time.sleep(300)
