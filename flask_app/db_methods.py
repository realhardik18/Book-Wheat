import ast
import redis
from creds import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def CheckIfUserExists(user_id):
    for key in redis_client.scan_iter():
        #print(str(key)[2:-1], user_id)
        if str(key)[2:-1] == str(user_id):
            return True


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
    return ast.literal_eval(str(redis_client.get(name=str(user_id)))[2:-1])


def GetAllCategories(user_id):
    data = ShowSpecifcUserData(user_id)
    categories = list()
    for category in data['categories']:
        categories.append(category['name'])
    return categories


def AddCategory(user_id, category_name):
    data = ShowSpecifcUserData(user_id)
    category_exists = False
    for category in data['categories']:
        if category['name'] == category_name:
            category_exists = True
    if len(data['categories']) == 0 or category_exists == False:
        new_category_data = {
            'name': category_name,
            'data': list()
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


def ShowCategoryData(user_id, category_name):
    data = ShowSpecifcUserData(user_id)
    for category in data['categories']:
        if category['name'] == category_name:
            return category['data']


#AddUser(user_id=1553622983142670336, username='bookwheat')
# print(ShowSpecifcUserData(user_id=1553622983142670336))
# print(CheckIfCategoryExits(user_id=1553622983142670336,category_name='water'))
