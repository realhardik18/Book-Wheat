import redis
from creds import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
#r.set('hello', 'hello')
r.acl_setuser(username='realhardik18')
