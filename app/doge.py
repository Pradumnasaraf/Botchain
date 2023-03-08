from requests.sessions import Session
import os
import tweepy
import time
import json
import requests
import typing
from dotenv import load_dotenv
load_dotenv()

# Add all the Key in the .env file according to the constant name.
consumer_key = os.environ.get('DOGE_CON_KEY')
consumer_secret = os.environ.get('DOGE_CON_SECRET')
key = os.environ.get('DOGE_KEY')
secret = os.environ.get('DOGE_SECRET')
coinAPIKey = os.environ.get('DOGE_COIN_KEY')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'slug': 'dogecoin',
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coinAPIKey
}

session = Session()
session.headers.update(headers)

Ticker = 1

while True:

    try:

        response = session.get(url, params=parameters)
        Data = json.loads(response.text)['data']['74']['quote']['USD']['price']
        formatted = '{0:.6g}'.format(Data)
        FinalMessage = 'Current #DOGE Price is $' + \
            str(formatted)+' #Dogecoin #Crypto #ToTheMoon🌕'
        api.update_status(FinalMessage)
        print('DOGE Tweet No.'+str(Ticker))
        Ticker = Ticker+1
        time.sleep(613)

    except tweepy.TweepError as e:
        
        print(e.reason)
        print('DOGE Tweet No.'+str(Ticker))
        Ticker = Ticker+1
        time.sleep(100)
