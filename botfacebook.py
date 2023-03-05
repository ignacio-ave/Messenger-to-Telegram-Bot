import requests
import json
import hmac
import hashlib

class Bot:
    def __init__(self, telegram_token):
        self.telegram_token = telegram_token

    def send_telegram_message(self, chat_id, message):
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(url, json=data)
        return response.json()

    def get_user_profile(self, sender_id):
        # Implementar esta función según corresponda
        pass

    def send_text_message(self, sender_id, message):
        # Implementar esta función según corresponda
        pass

class FacebookBot:
    def __init__(self, bot, fb_token, app_secret):
        self.bot = bot
        self.fb_token = fb_token
        self.app_secret = app_secret

    def verify_fb_token(self, x_hub_signature, request_data, token):
        expected_signature = hmac.new(
            bytes(self.app_secret, 'latin-1'),
            msg=request_data,
            digestmod=hashlib.sha1
        ).hexdigest()

        return hmac.compare_digest(x_hub_signature.split('=')[1], expected_signature)

    def handle_message(self, sender_id, message):
        if message.lower() == "ayuda":
            response = "¡Bienvenido! Puede escribir un número del 1 al 3 para obtener una respuesta."
            self.bot.send_text_message(sender_id, response)
        elif message.isnumeric():
            number = int(message)
            if number == 1:
                response = "La respuesta para el número 1 es ..."
                self.bot.send_text_message(sender_id, response)
            else:
                response = "Lo siento, solo puedo manejar números del 1 al 3."
                self.bot.send_text_message(sender_id, response)
        elif message == "estoy interesado":
            # Obtener información del usuario y trabajo
            user_profile = self.bot.get_user_profile(sender_id)
            nombre = user_profile["first_name"]
            apellido = user_profile["last_name"]
            trabajo = "trabajo"
            # Enviar notificación a Telegram
            mensaje = f"{nombre} {apellido} está interesado en {trabajo}"
            chat_id = "ID_DE_CHAT_DE_TELEGRAM"
            self.bot.send_telegram_message(chat_id, mensaje)
            # Responder al usuario
            respuesta = "Gracias por su interés. Nos pondremos en contacto con usted pronto."
            self.bot.send_text_message(sender_id, respuesta)
        else:
            respuesta = "Lo siento, no entendí su mensaje."
            self.bot.send_text_message(sender_id, respuesta)

    def handle_webhook(self, request):
        if request.method == "POST":
            # Verificar la firma del webhook
            x_hub_signature = request.headers.get("X-Hub-Signature")
            request_data = request.data
            if not self.verify_fb_token(x_hub_signature, request_data, self.fb_token):
                abort(400)

            # Manejar el evento de webhook
            data = request.get_json()
            if data["object"] == "page":
                for entry in data["entry"]:
                    for event in entry["messaging"]:
                        if "message" in event:
                            sender_id = event["sender"]["id"]
                            message = event["message"]
                            if "text" in message:
                                text = message["text"]
                                self.handle_message(sender_id, text)

        return "OK"
