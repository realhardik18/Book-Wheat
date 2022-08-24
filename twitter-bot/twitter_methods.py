import ast
import redis
from creds import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT
import requests

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def GetLastCheckedTweetID():
    return int(redis_client.get('last_seen'))


def UpdateLastCheckedTweetID(tweet_id):
    redis_client.set('last_seen', tweet_id)


def GetTweetInfo(tweet_url):
    resp = requests.get(
        f"https://publish.twitter.com/oembed?url={tweet_url}")
    relevant_data = {
        'url': resp.json()['url'],
        'author': resp.json()['author_name'],
        'author_url': resp.json()['author_url']

    }
    return relevant_data


# UpdateLastCheckedTweetID(1561343519364911104)
# print(GetLastCheckedTweetID())
# UpdateLastCheckedTweetID(1562432456510189568)
