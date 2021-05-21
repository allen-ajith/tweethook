import requests
import json
# import configtoken           ##contains bearer token
import tweepy, sys
from random import randint
from os import environ

# CONSUMER_KEY = configtoken.keys['consumer_key']
# CONSUMER_SECRET = configtoken.keys['consumer_secret']
# ACCESS_TOKEN = configtoken.keys['access_token']
# ACCESS_TOKEN_SECRET = configtoken.keys['access_token_secret']

CONSUMER_KEY = environ['consumer_key']
CONSUMER_SECRET = environ['consumer_secret']
ACCESS_TOKEN = environ['access_token']
ACCESS_TOKEN_SECRET = environ['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# handle = 'MadavanaB'
# user_id = api.get_user(handle).id_str
# message = 'hello, testing again from tweepy'
# dm = api.send_direct_message(recipient_id = user_id,text = message)
# print(dm.message_create['message_data']['text'])

def create_url_tweets():
    return "https://api.twitter.com/2/tweets/search/stream?tweet.fields=in_reply_to_user_id,author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

# def create_url_users(authID):
#     return "https://api.twitter.com/2/users?ids="+str(authID)+"&user.fields=profile_image_url"

# def create_url_parent_tweets(refTweet):
#     return "https://api.twitter.com/2/tweets?ids="+str(refTweet["id"])+"&tweet.fields=author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

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
                    dm = api.send_direct_message(recipient_id = authID,text = message)
                    print(dm.message_create['message_data']['text'])
        except:
            print("calling again")
            return "callagain"


# def get_all_parents(refTweet,headers):
#     url = create_url_parent_tweets(refTweet)
#     response = requests.request("GET", url, headers=headers)
#     print('twitter parent response: ',response.status_code)
#     # print(response.headers)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     else:
#         json_response = json.loads(response.content)
#         print(json.dumps(json_response, indent =4,sort_keys=True))
#         authID = json_response["data"][0]["author_id"]
#         connect_to_endpoint_users(authID,headers)
#         store_tweet_data(json_response)
#         if(json_response["data"][0]["id"]!=json_response["data"][0]["conversation_id"]):
#             get_all_parents(json_response["data"][0]["referenced_tweets"][0],headers)


# def connect_to_endpoint_users(authID, headers):
#     url = create_url_users(authID)
#     response = requests.request("GET", url, headers=headers)
#     print('user response: ',response.status_code)
#     # print(response.headers)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     else:
#         json_response = json.loads(response.content)
#         # store_user_data(json_response)
#         print(json.dumps(json_response,indent=4))


# def store_tweet_data(json_response):
#     data=dict()
#     for key,value in json_response["data"].items():
#         data[key]= value
#     if "referenced_tweets" not in data:
#         data["referenced_tweets"] = [{"id":"none","type":"none"}]
#     print(json.dumps(data, indent =4,sort_keys=True))



# def store_user_data(json_response):
#     data=dict()
#     for key,value in json_response["data"][0].items():
#         data[key]= value
#     print(json.dumps(data, indent =4,sort_keys=True))





def main():
    bearer_token = environ['brToken']
    url = create_url_tweets()
    headers = create_headers(bearer_token)
    timeout = 0
    error = connect_to_endpoint_tweet(url=url,headers=headers)
    if error == "callagain":
        connect_to_endpoint_tweet(url=url,headers=headers)


if __name__ == "__main__":
    main()