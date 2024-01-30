import telegram 

TOKEN='6804364814:AAFG6WL6EcqnIgL_9qY4euWHUcvGaCKLU08'

bot = telegram.Bot(TOKEN)

URL = 'https://jahongir5051.pythonanywhere.com/'

# bot.delete_webhook()
# bot.setWebhook(URL)

print(bot.get_webhook_info())