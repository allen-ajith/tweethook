import requests
import os
import json
import configtoken  ##contains bearer token
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


# urlSendDataTweets = ""

def auth():
    # print(str(os.environ.get("BEARER_TOKEN")))
    return str(os.environ.get("BEARER_TOKEN"))


def create_url_tweets():
    return "https://api.twitter.com/2/tweets/search/stream?tweet.fields=author_id,referenced_tweets,conversation_id,public_metrics,created_at,source"

def create_url_users(authID):
    return "https://api.twitter.com/2/users?ids="+str(authID)+"&user.fields=profile_image_url"


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint_tweet(url, headers):
    response = requests.request("GET", url, headers=headers, stream=True)
    print('twitter response: ',response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # print(json.dumps(json_response, indent =4,sort_keys=True))
            authID = json_response["data"]["author_id"]
            refTweet = json_response["data"]["referenced_tweets"][0]
            convID = json_response["data"]["conversation_id"]
            post_tweet_data(json_response)
            connect_to_endpoint_users(authID,headers)
            if "referenced_tweets" in json_response["data"]:
                get_all_parents(refTweet,convID)


def get_all_parents(refTweet,convID):
    print("hello")


def connect_to_endpoint_users(authID, headers):
    url = create_url_users(authID)
    response = requests.request("GET", url, headers=headers)
    print('user response: ',response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    else:
        json_response = json.loads(response.content)
        post_user_data(json_response)
        # print(json.dumps(responseJson,indent=4))


def post_tweet_data(json_response):
    data=dict()
    for key,value in json_response["data"].items():
        data[key]= value
    if "referenced_tweets" not in data:
        data["referenced_tweets"] = [{"id":"none","type":"none"}]
    print(json.dumps(data, indent =4,sort_keys=True))
    # requests.post(urlSendDataTweets, data=data)


def post_user_data(json_response):
    data=dict()
    for key,value in json_response["data"][0].items():
        data[key]= value
    print(json.dumps(data, indent =4,sort_keys=True))
    # requests.post(urlSendDataUsers, data=data)




def main():
    bearer_token = configtoken.brToken
    print(configtoken.brToken)
    url = create_url_tweets()
    headers = create_headers(bearer_token)
    timeout = 0
    while True:
        connect_to_endpoint_tweet(url, headers)
        timeout += 1
        # print('timeout: ',timeout)


if __name__ == "__main__":
    main()