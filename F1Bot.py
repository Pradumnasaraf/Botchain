import tweepy
import time
               
auth = tweepy.OAuthHandler('95IVnwKaS1kH99tUX5ms1Loe4','vFkwVcZ5fHGmBpXfoRk5iVNrNzFh5RwVu0mL717cKhNpRB6d6b')
auth.set_access_token('1434857266247729158-tXWHFHE52W5mR24KZt9lo3xrCcdhK6','dHaZx4Ebja0xqgvBnpIMravspdIVaIet7f8cXOLdv2jyN')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_term = '#f1'
TweetNumber = 250

tweets = tweepy.Cursor(api.search,search_term).items()# Argumnets =TweetNumber

#Counter to keep track of no of tweets
count =0

# Taking out a tweets from the Array of tweet.
for tweet in tweets:
    count = count +1

    #After tweeting for 50 tweets Bot will sleep for 60 Seconds.
    if count ==50:
        count =0
        time.sleep(250)

    #Try to like the tweet
    try:
        print('Tweet Liked NO- '+ str(count))
    
        #favorite() method is liking the tweet
        tweet.favorite()

        # After every like bot is sleeping for 5 Seconds.
        time.sleep(5)

    # Handeling any kind of exception (eg; tweet already liked some limitation error) 
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(5)
