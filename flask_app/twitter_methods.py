import ast
import redis
from creds import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import requests
import tweepy


twitter_client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                               access_token=ACCESS_KEY, access_token_secret=ACCESS_SECRET)
redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def GetLastCheckedTweetID():
    return int(redis_client.get('last_seen'))


def UpdateLastCheckedTweetID(tweet_id):
    redis_client.set('last_seen', tweet_id)


def GetEmbededTweetHTML(tweet_url):
    resp = requests.get(
        f"https://publish.twitter.com/oembed?url={tweet_url}&theme=dark&conversation=none&cards=hidden&hide_media=true")
    return f"<center>{resp.json()['html']}<center>"


def GetTweetInfo(tweet_url):
    resp = requests.get(
        f"https://publish.twitter.com/oembed?url={tweet_url}")
    relevant_data = {
        'url': resp.json()['url'],
        'author': resp.json()['author_name'],
        'author_url': resp.json()['author_url']

    }
    return relevant_data


# print(GetTweetInfo("https://twitter.com/Book_Wheat/status/1561347864827203589"))
