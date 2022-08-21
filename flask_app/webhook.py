from urllib import request
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
#from creds import WEB_HOOK_URL


def initializeWebHook(webhook_url):
    try:
        content = 'hello'
        weebhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title='Initialized channle',
                             description='Now all the tweets will come here')
        weebhook.add_embed(embed=embed)
        response = weebhook.execute()
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False
