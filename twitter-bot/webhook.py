from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import random
from twitter_methods import GetTweetInfo
#from creds import WEB_HOOK_URL


def initializeWebHook(webhook_url):
    try:
        #content = 'hello'
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


def sendMessage(webhook_url, tweet_url):
    all_colors = [
        0x1abc9c,
        0x11806a,
        0x2ecc71,
        0x1f8b4c,
        0x3498db,
        0x206694,
        0x9b59b6,
        0x71368a,
        0xe91e63,
        0xad1457,
        0xf1c40f,
        0xc27c0e,
        0xe67e22,
        0xa84300,
        0xe74c3c,
        0x992d22,
        0x95a5a6,
        0x607d8b,
        0x979c9f,
        0x546e7a,
        0x7289da,
        0x99aab5
    ]
    data = GetTweetInfo(tweet_url=tweet_url)
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="New saved tweet!",
                         description=f"[click here]({data['url']}) to see the tweet from [{data['author']}]({data['author_url']})", color=random.choice(all_colors))
    embed.set_footer(text='powered by @Book_Wheat',
                     icon_url="https://pbs.twimg.com/profile_images/1560373455358308352/afJgVviC_400x400.jpg")
    webhook.add_embed(embed=embed)
    webhook.execute()
