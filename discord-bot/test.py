from discord_webhook import DiscordWebhook, DiscordEmbed
from creds import WEB_HOOK_URL
content = 'hello'
weebhook = DiscordWebhook(
    url=WEB_HOOK_URL)
embed = DiscordEmbed(title='test', description='content')
weebhook.add_embed(embed=embed)
response = weebhook.execute()
