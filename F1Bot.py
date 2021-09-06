import tweepy
import time

from tweepy import cursor
               
auth = tweepy.OAuthHandler('95IVnwKaS1kH99tUX5ms1Loe4','vFkwVcZ5fHGmBpXfoRk5iVNrNzFh5RwVu0mL717cKhNpRB6d6b')
auth.set_access_token('1434857266247729158-tXWHFHE52W5mR24KZt9lo3xrCcdhK6','dHaZx4Ebja0xqgvBnpIMravspdIVaIet7f8cXOLdv2jyN')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#f1'
search1 = '#formula1'
noTweet = 500

for tweet in tweepy.Cursor(api.search, search).items(noTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopAsyncIteration:
        break