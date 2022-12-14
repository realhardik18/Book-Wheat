import tweepy
# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.create_tweet
from creds import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from twitter_methods import GetLastCheckedTweetID, UpdateLastCheckedTweetID
from db_methods import GetAllCategories, AddTweetInCategory, AddCategory, CheckIfUserExists, AddUser, ReturnWebhook, ShowSpecifcUserData, GetRepliedTweetsIds, AddInRepliedTweetsList
from webhook import sendMessage
import time
import random
import json
client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY, access_token_secret=ACCESS_SECRET)


def tweet(tweet_content):
    client.create_tweet(tweet_content)


def reply_to_tweet(tweet_to_reply_to_id, tweet_content):
    client.create_tweet(
        in_reply_to_tweet_id=tweet_to_reply_to_id, text=tweet_content, user_auth=True)


def like_tweet(tweet_to_like_id):
    client.like(tweet_to_like_id)


def search_mentions(last_tweet_id):
    return client.get_users_mentions(id=1474790376259031044, since_id=last_tweet_id, expansions='referenced_tweets.id,referenced_tweets.id.author_id', user_auth=True)


def get_tweet(id):
    return client.get_tweet(id, user_auth=True)


'''
tweet = list(search_mentions()[0])[0]
# print(tweet)
base_url = 'https://twitter.com/'
main_tweet = tweet.data['referenced_tweets'][0]
# print(main_tweet)
data = client.get_tweet(id=main_tweet['id'],
                        user_auth=True, expansions='author_id')
parent_tweet_id = str(list(data)[0]['id'])
parent_user_name = str(list(data)[1]['users'][0])
url_to_tweet = base_url+parent_user_name+'/'+'status/'+parent_tweet_id
print(url_to_tweet)

for tweet in search_mentions()[0]:
    with open('seen.json') as json_file:
        data = json.load(json_file)
        data['seen_tweet_ids'].append(tweet.id)
    with open('seen.json', 'w') as outfile:
        json.dump(data, outfile)
'''
print('hello there')
while True:
    replied_to = list()
    mentioned_tweets = search_mentions(
        last_tweet_id=GetLastCheckedTweetID())[0]
    if mentioned_tweets != None:
        #print('ello', type(mentioned_tweets))
        for tweet in mentioned_tweets:
            if tweet.id not in replied_to:
                UpdateLastCheckedTweetID(tweet.id)
                base_url = 'https://twitter.com/'
                try:
                    # print(GetRepliedTweetsIds())
                    # print(type(str(tweet.id)))
                    # if str(tweet.id) not in GetRepliedTweetsIds():
                    print(f"{tweet.id} was not there so i added it!")
                    main_tweet = tweet.data['referenced_tweets'][0]
                    data = client.get_tweet(id=main_tweet['id'],
                                            user_auth=True, expansions='author_id')
                    parent_tweet_id = str(list(data)[0]['id'])
                    parent_user_name = str(list(data)[1]['users'][0])
                    url_to_tweet = base_url+parent_user_name+'/'+'status/'+parent_tweet_id
                    #print(tweet.text, tweet.author_id)
                    # print(url_to_tweet)
                    '''
                    if str(tweet.author_id) not in profiles['users'].keys():
                        profiles['users'][str(tweet.author_id)] = list()
                    #to check if user exists
                    '''

                    data_dict = dict()
                    # data_dict['saved_at'] = tweet.created_at WORK ON THIS LATER
                    url_to_tweet = url_to_tweet
                    category = ' '.join(tweet.text.split(
                        ' ')[tweet.text.split(' ').index('@Book_Wheat')+1:])
                    # profiles['users'][str(tweet.author_id)].append(data_dict)
                    if CheckIfUserExists(user_id=str(tweet.author_id)) == False:
                        AddUser(user_id=str(tweet.author_id), username=list(client.get_user(id=tweet.author_id,
                                                                                            user_auth=True))[0].username)
                        # time.sleep(2)
                    all_categories = GetAllCategories(str(tweet.author_id))
                    # print(all_categories,str(tweet.author_id))
                    # time.sleep(2)

                    if category in all_categories and len(all_categories) != 0:
                        AddTweetInCategory(user_id=str(
                            tweet.author_id), category_name=category, url_to_tweet=url_to_tweet)
                    else:
                        AddCategory(user_id=str(tweet.author_id),
                                    category_name=category)
                        AddTweetInCategory(user_id=str(
                            tweet.author_id), category_name=category, url_to_tweet=url_to_tweet)
                    # print(ReturnWebhook(user_id=str(
                        # tweet.author_id), category_name=category))
                    if ReturnWebhook(user_id=str(tweet.author_id), category_name=category) != None:
                        sendMessage(webhook_url=ReturnWebhook(user_id=str(
                            tweet.author_id), category_name=category), tweet_url=url_to_tweet)
                        tweet_content = f"Saved the tweet! [category name->{category} ({''.join(random.choice('0123456789ABCDEF') for i in range(4))})]\nI have also sent the tweet to the discord channle associated to this category!"
                    else:
                        tweet_content = f"Saved the tweet! [category name->{category} ({''.join(random.choice('0123456789ABCDEF') for i in range(4))})]"
                    reply_to_tweet(tweet_to_reply_to_id=tweet.id,
                                   tweet_content=tweet_content)
                    # print(ShowSpecifcUserData(user_id=str(tweet.author_id)))
                    # print(list(client.get_user(id=tweet.author_id,user_auth=True))[0].username)
                    replied_to.append(tweet.id)
                    time.sleep(10)
                except KeyError:
                    print('oops')
            else:
                print('no new ttweet')
    else:
        print('no new tweets')
        time.sleep(5)
