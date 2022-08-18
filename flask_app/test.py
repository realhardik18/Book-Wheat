import requests

resp = requests.get(
    "https://publish.twitter.com/oembed?url=https://twitter.com/WSJ/status/1560344542590763012")
print(resp.json())
