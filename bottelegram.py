import telegram
from flask import Flask, request, abort

app = Flask(__name__)
bot = telegram.Bot(token='tu_token_de_acceso_al_bot_de_telegram')
chat_id = 'tu_chat_id'

@app.route('/telegram', methods=['POST'])
def telegram_webhook():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        handle_update(update)
    return 'ok'

def handle_update(update):
    text = update.message.text.lower()
    if text == 'estoy interesado':
        user_name = update.message.from_user.first_name
        job = 'El trabajo en el que está interesado'
        message = f'{user_name} está interesado en {job}.'
        bot.send_message(chat_id=chat_id, text=message)

if __name__ == '__main__':
    app.run()
'''

## Ejemplo de uso

```python 
import telegram

bot = telegram.Bot(token='tu_token_de_acceso_al_bot_de_telegram')
chat_id = 'tu_chat_id'

bot.send_message(chat_id=chat_id, text='Hola, soy un bot de Telegram')
```

## Referencias

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
