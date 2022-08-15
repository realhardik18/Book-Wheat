import requests as r
import json
import ast
from flask import render_template, Flask, redirect, url_for, request
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
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
    return str(resp.text)


app.run(debug=True)
