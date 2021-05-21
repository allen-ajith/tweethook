from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date 
from os import environ
from tweetHook import(create_headers,create_url_tweets,connect_to_endpoint_tweet)
sched = BackgroundScheduler()
def bot():
    bearer_token = environ['brToken']
    url = create_url_tweets()
    headers = create_headers(bearer_token)
    timeout = 0
    error = connect_to_endpoint_tweet(url=url,headers=headers)
    if error == "callagain":
        connect_to_endpoint_tweet(url=url,headers=headers)

sched.add_job(bot,'date',run_date=date(2021,5,21),args=['text'])
sched.start