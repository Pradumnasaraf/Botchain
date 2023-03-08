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
consumer_key = os.environ.get('BTC_CON_KEY')
consumer_secret = os.environ.get('BTC_CON_SECRET')
key = os.environ.get('BTC_KEY')
secret = os.environ.get('BTC_SECRET')
coinAPIKey = os.environ.get('BTC_COIN_KEY')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'slug': 'bitcoin',
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
        Data = json.loads(response.text)['data']['1']['quote']['USD']['price']
        FinalMessage = 'Current #Bitcoin Price is $' + \
            str(round(Data))+' #BTC #Crypto'
        api.update_status(FinalMessage)
        print('BTC Tweet No.'+str(Ticker))
        Ticker = Ticker+1
        time.sleep(613)

    except tweepy.TweepError as e:

        print(e.reason)
        time.sleep(100)
