# this program utilizes twitter's API to analyze people''s sentiments on twitter on a given subject

# first we import our dependencies
import tweepy
from textblob import TextBlob

#get these from your twitter's developer account
consumer_key = 'xxxxxxx'
consumer_secret = 'xxxxxxx'

access_token = 'xxxxxx'
access_token_secret = 'xxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )

api = tweepy.API(auth)

#add your desired subject below
public_tweets = api.search('subject')

#this gives you tweets on the subject as well as the objectivity and truthfulness of the tweet both on a scale of -2 to 2
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')
