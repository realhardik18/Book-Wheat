import ast
import redis
from creds import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def GetLastCheckedTweetID():
    return int(redis_client.get('last_seen'))


def UpdateLastCheckedTweetID(tweet_id):
    redis_client.set('last_seen', tweet_id)


# print(GetLastCheckedTweetID())
