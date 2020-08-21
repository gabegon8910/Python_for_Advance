from discord_webhook impoer DiscordWebhook

message = "Hello There"
webhook = DiscordWebhook(url="URL", content=message)
response = webhook.execute()
