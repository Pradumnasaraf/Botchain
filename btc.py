from requests.sessions import Session
import tweepy
import time
import json
import requests
import typing

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
Ticker =1

url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters={
    'slug':'bitcoin',
}

headers ={
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY':''
}
session = Session()
session.headers.update(headers)

while True:

    try:
        response = session.get(url,params=parameters)
        Data = json.loads(response.text)['data']['1']['quote']['USD']['price']
        FinalMessage = 'Current #Bitcoin Price is $'+ str(round(Data))+' #BTC #Crypto'
        api.update_status(FinalMessage)

        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1

        time.sleep(300)


    except tweepy.TweepError as e:
        print(e.reason)
        print('Tweet No.'+str(Ticker))
        Ticker= Ticker+1
        time.sleep(300)
