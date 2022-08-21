import ast
import redis
from creds import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def CheckIfUserExists(user_id):
    for key in redis_client.scan_iter():
        # print(str(key)[2:-1], user_id)
        if str(key)[2:-1] == str(user_id):
            return True
    return False


def DeleteAllUsers():
    for key in redis_client.scan_iter():
        redis_client.delete(key)


def ShowAllUsers():
    users = list()
    for user in redis_client.keys():
        users.append(str(user)[2:-1])
    return users


def AddUser(user_id, username):
    initial_user_data = {
        'username': username,
        'categories': list()
    }
    redis_client.set(name=str(user_id), value=str(initial_user_data))


def ShowSpecifcUserData(user_id):
    # print(f'HELLO\n{str(redis_client.get(name=str(user_id)))[2:-1]}\nhello')
    return ast.literal_eval(str(redis_client.get(name=str(user_id)))[2:-1])
    # return str(redis_client.get(name=str(user_id)))[2:-1]


def GetAllCategories(user_id):
    data = ShowSpecifcUserData(str(user_id))
    return data['categories']


def AddCategory(user_id, category_name):
    data = ShowSpecifcUserData(user_id)
    category_exists = False
    for category in data['categories']:
        if category['name'] == category_name:
            category_exists = True
    if len(data['categories']) == 0 or category_exists == False:
        new_category_data = {
            'name': category_name,
            'data': list(),
            'webhookURL': None
        }
        data['categories'].append(new_category_data)
        redis_client.set(user_id, str(data))
    elif category_exists == True:
        return 'exists'


def DeleteUser(user_id):
    redis_client.delete(str(user_id))


def AddTweetInCategory(user_id, category_name, url_to_tweet):
    data = ShowSpecifcUserData(user_id)
    for category in data['categories']:
        if category['name'] == category_name:
            category['data'].append(url_to_tweet)
            redis_client.set(user_id, str(data))
            break


def ReturnWebhook(user_id, category_name):
    data = ShowSpecifcUserData(user_id)
    for category in data['categories']:
        if category['webhookURL'] != None:
            return category['webhookURL']
    return None
# AddUser(user_id=1065343305993588736, username='test')
# print(ShowSpecifcUserData(user_id=1065343305993588736))
# print(CheckIfUserExists(1553622983142670336))
# print(ShowSpecifcUserData(user_id=1553622983142670336))
# print((GetAllCategories(user_id=1065343305993588736)))
# print(len(GetAllCategories(str(1065343305993588736))),
# type(GetAllCategories(str(1065343305993588736))))
# DeleteUser(user_id=1553622983142670336)
