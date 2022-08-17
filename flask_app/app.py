import requests as r
import json
import ast
from flask import render_template, Flask, redirect, url_for, request
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from db_methods import ShowSpecifcUserData
from creds import API_KEY, API_SECRET, APP_SECRET_KEY

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
blueprint = make_twitter_blueprint(
    api_key=API_KEY,
    api_secret=API_SECRET,
)
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("https://api.twitter.com/2/users/me")
    user_id = ast.literal_eval(str(resp.text))['data']['id']
    data = ShowSpecifcUserData(user_id=user_id)
    return render_template('index.html', username=data['username'], category_data=data['categories'])
# work from here
# work on checking if user exits and logic and ui


app.run(debug=True)

'''
TODO
MAKE LOGO
AND UI IN A BETTER MANNER
'''
