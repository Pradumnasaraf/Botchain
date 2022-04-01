from requests.sessions import Session
import os
import tweepy
import time
import json
import requests
import typing
from dotenv import load_dotenv
load_dotenv()

# We will get all of these sceret keys from twitter developer account

consumer_key = os.environ.get('DOGE_CON_KEY')
consumer_secret = os.environ.get('DOGE_CON_SECRET')
key = os.environ.get('DOGE_KEY')
secret = os.environ.get('DOGE_SECRET')
coinAPIKey = os.environ.get('DOGE_COIN_KEY')

# we pass our consumer key and secret for authentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

# This is optional, it's used to rate limit.
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# API Request URL
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Here dpgecoin is used as a para, we can provide any documented ticker.
parameters={
    'slug':'dogecoin',
}

headers ={
    # Here we are specifying the the data format, in which we want to fetch the data.
    'Accepts': 'application/json',

    # CoinMaket API Key
    'X-CMC_PRO_API_KEY': coinAPIKey
}

# Its is simply a kind of browsing seession, use to save reapted info like cookies, beacuse requested data (type) with always be same.
session = Session()
session.headers.update(headers)

# To keep track of no of the tweet, the bot has tweeted
Ticker =1

# Using a loop for getting the latest price, by requesting the API after a fixed amount of time.
while True:

    # We cover the whole thing in the try-except block so that we can handle the error, rather than terminating the program.
    try:
        # Trying to get data and parsing it.
        response = session.get(url,params=parameters)
        Data = json.loads(response.text)['data']['74']['quote']['USD']['price']

        # we need the value upto only 6 decimal places.
        formatted = '{0:.6g}'.format(Data)

        # This is the exact message that will go on Twitter.
        FinalMessage = 'Current #DOGE Price is $'+str(formatted)+' #Dogecoin #Crypto #ToTheMoon🌕'

        # Tweeting out the FinalMessage.
        api.update_status(FinalMessage)

        # Printing the no of tweets that happened on the terminal
        print('DOGE Tweet No.'+str(Ticker))

        # Updating the ticker
        Ticker= Ticker+1

        # Bot will sleep for 5 minutes after every single, tweet
        time.sleep(300)

    # Exception handeling 
    except tweepy.TweepError as e:

        # Print the root cause of the error
        print(e.reason)
        print('DOGE Tweet No.'+str(Ticker))
        
        # Updating the ticker
        Ticker= Ticker+1
        time.sleep(100)