from flask import Flask
import telegram

app = Flask(__name__)

TOKEN='6804364814:AAFG6WL6EcqnIgL_9qY4euWHUcvGaCKLU08'

bot = telegram.Bot(TOKEN)

chat_id='927181585'

@app.route('/')
def hello_world():
    bot.send_message(chat_id , 'Hello World!!!')
    return 'Hello World!!'
