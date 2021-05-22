import requests,json, tweepy
from random import randint
import os
from boto.s3.connection import S3Connection

CONSUMER_KEY = os.environ['consumer_key']
CONSUMER_SECRET = os.environ['consumer_secret']
ACCESS_TOKEN = os.environ['access_token']
ACCESS_TOKEN_SECRET = os.environ['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def create_url_tweets():
    return "https://api.twitter.com/2/tweets/search/stream?tweet.fields=in_reply_to_user_id,author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint_tweet(url, headers):
    response = requests.request("GET", url, headers=headers, stream=True)
    print('twitter response: ',response.status_code)
    # print(response.headers)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    else:
        try:
            for response_line in response.iter_lines():
                if response_line:
                    json_response = json.loads(response_line)
                    print(json.dumps(json_response, indent =4,sort_keys=True))
                    authID = json_response["data"]["author_id"]
                    parentTwtID = json_response["data"]["referenced_tweets"][0]["id"]
                    parentauthor = json_response["data"]["in_reply_to_user_id"]
                    message = "https://twitter.com/"+parentauthor+"/status/"+parentTwtID
                    # message="hello, you are gay"
                    try:
                        dm = api.send_direct_message(recipient_id = authID,text = message)
                        print(dm.message_create['message_data']['text'])
                    except tweepy.TweepError as e:
                        print("ThreaderBot:Error in sending '{}' as dm response, {}".format(message,e))
        except:
            print("calling again")
            return "callagain"


def main():
    bearer_token = os.environ['brToken']
    url = create_url_tweets()
    headers = create_headers(bearer_token)
    timeout = 0
    error = connect_to_endpoint_tweet(url=url,headers=headers)
    if error == "callagain":
        connect_to_endpoint_tweet(url=url,headers=headers)


if __name__ == "__main__":
    main()