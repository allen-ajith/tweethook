import tweepy, sys, time
from random import randint

keys = {"consumer_key": "LFsJb4hVhbm9goH0nkcbykv4x","consumer_secret": "nRgkWf4lb6LwCrrHZtAnnSEV1panwSiikaCrIFFs7rXLR48KzG", "access_token": "1393850500504637440-rlcFiq9GLsjdeulQ7FpZUVthtar8Vj","access_token_secret": "HEq8Lr3BvXjmwfYfuWc3j4ePcQSWkYl24qHfgQftMPYPf"}

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


handle = 'MadavanaB'
user_id = api.get_user(handle).id_str
print(type(user_id))
message = 'hello, testing from tweepy'
dm = api.send_direct_message(recipient_id=str(1395639903443046404), text=message)
print(dm.message_create['message_data']['text'])