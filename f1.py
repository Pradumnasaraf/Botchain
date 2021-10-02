import tweepy
import time

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_term = '#F1'
TweetNumber = 990
counter =1
tweets = tweepy.Cursor(api.search,search_term).items(TweetNumber)# Argumnets =TweetNumber

# Taking out a tweets from the Array of tweet.
for tweet in tweets:
        if counter ==40:
            print('Bot is Sleeping for 30 Minutes')
            time.sleep(1800)
            counter =1

        #Try to like the tweet
        try:
            #Checking the tweet weather its fav or not
            if tweet.favorited is False:
                print('Tweet Liked '+str(counter))
                tweet.favorite()
                counter = counter +1
                time.sleep(45)


        # Handeling any kind of exception (eg; tweet already liked some limitation error)
        except tweepy.TweepError as e:
            counter = counter +1
            print(e.reason)
            time.sleep(45)