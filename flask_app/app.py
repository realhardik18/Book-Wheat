import requests as r
import json
import ast
from flask import render_template, Flask, redirect, url_for, request
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from db_methods import ShowSpecifcUserData, CheckIfUserExists, AddUser, GetAllCategories, ShowCategoryData
from creds import API_KEY, API_SECRET, APP_SECRET_KEY
from twitter_methods import GetEmbededTweetHTML

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
blueprint = make_twitter_blueprint(
    api_key=API_KEY,
    api_secret=API_SECRET,
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/home")
def home():
    if not twitter.authorized:
        return render_template('login.html')
    resp = twitter.get("https://api.twitter.com/2/users/me")
    user_id = ast.literal_eval(str(resp.text))['data']['id']
    username = ast.literal_eval(str(resp.text))['data']['username']
    if CheckIfUserExists(user_id=user_id) == None:
        AddUser(user_id=user_id, username=username)
    data = ShowSpecifcUserData(user_id=user_id)
    return render_template('home.html', username=data['username'], category_data=data['categories'])


@app.route("/")
def index():
    if not twitter.authorized:
        return render_template('login.html')
    return redirect(url_for('home'))


@app.route('/category/<name>')  # /landingpage/A
def tweet_data(name):
    if not twitter.authorized:
        return render_template('login.html')
    resp = twitter.get("https://api.twitter.com/2/users/me")
    user_id = ast.literal_eval(str(resp.text))['data']['id']
    username = ast.literal_eval(str(resp.text))['data']['username']
    if name in GetAllCategories(user_id=user_id):
        tweets = ShowCategoryData(user_id=user_id, category_name=name)
        data = ShowSpecifcUserData(user_id=user_id)
        html_data = list()
        for tweet in tweets:
            html_data.append(GetEmbededTweetHTML(tweet))
        return render_template('data.html', tweets=tweets, category_name=name, username=data['username'], html_codes=html_data)
    return redirect(url_for('home'))

    # work from here
    # work on checking if user exits and logic and ui


# app.run(debug=True)

'''
TODO
MAKE LOGO
AND UI IN A BETTER MANNER
'''

# WORK ONLY AND ONLY ON THIS AND FINSH IT UP AND SUBMIT BEFORE WORKING
# ON DISCORD PART!
# USE BOOTSTRAP STFU
# AND HOST SITE
