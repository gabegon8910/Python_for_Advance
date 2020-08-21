# you will neeed to install discord webhook with pip install python-webhook

from discord_webhook impoer DiscordWebhook

message = "Hello There"
webhook = DiscordWebhook(url="URL", content=message)
response = webhook.execute()
