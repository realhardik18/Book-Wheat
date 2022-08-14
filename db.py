from ast import Delete
import redis
from creds import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD,)

# add stuff with r.set and work on retriving for the same
