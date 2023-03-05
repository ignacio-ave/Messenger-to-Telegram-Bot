import telegram
from flask import Flask, request, abort
import hmac
from hashlib import sha1

class BotTelegram:
    def __init__(self, token, id_chat):
        self.bot = telegram.Bot(token=token)
        self.id_chat = id_chat

    def enviar_mensaje(self, mensaje):
        self.bot.send_message(chat_id=self.id_chat, text=mensaje)

class WebhookTelegram:
    def __init__(self, bot, app, clave_secreta):
        self.bot = bot
        self.app = app
        self.clave_secreta = clave_secreta

        @app.route('/telegram', methods=['POST'])
        def telegram_webhook():
            if request.method == 'POST':
                signature = request.headers.get('X-Hub-Signature')
                if not self.verificar_firma(signature, request.data, self.clave_secreta):
                    abort(400)
                update = telegram.Update.de_json(request.get_json(force=True), bot.bot)
                self.procesar_actualizacion(update)
            return 'ok'

    def procesar_actualizacion(self, actualizacion):
        texto = actualizacion.message.text.lower()
        if texto == 'estoy interesado':
            nombre_usuario = actualizacion.message.from_user.first_name
            trabajo = 'El trabajo en el que está interesado'
            mensaje = f'{nombre_usuario} está interesado en {trabajo}.'
            self.bot.enviar_mensaje(mensaje)

    def verificar_firma(self, firma, datos, clave_secreta):
        clave_bytes = bytes(clave_secreta, 'latin-1')
        mac = hmac.new(clave_bytes, msg=datos, digestmod=sha1)
        return hmac.compare_digest('sha1=' + mac.hexdigest(), firma)

if __name__ == '__main__':
    app = Flask(__name__)
    bot = BotTelegram(token='tu_token_de_acceso_al_bot_de_telegram', id_chat='tu_id_de_chat')
    webhook = WebhookTelegram(bot, app, 'tu_clave_secreta')
    app.run()
