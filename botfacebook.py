import requests
import json

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
    def __init__(self, bot, fb_token):
        self.bot = bot
        self.fb_token = fb_token

    def verify_fb_token(self, x_hub_signature, request_data, token):
        # Implementar esta función según corresponda
        pass

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
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            job = "trabajo"
            # Enviar notificación a Telegram
            message = f"{first_name} {last_name} está interesado en {job}"
            chat_id = "ID_DE_CHAT_DE_TELEGRAM"
            self.bot.send_telegram_message(chat_id, message)
            # Responder al usuario
            response = "Gracias por su interés. Nos pondremos en contacto con usted pronto."
            self.bot.send_text_message(sender_id, response)
        else:
            response = "Lo siento, no entendí su mensaje."
            self.bot.send_text_message(sender_id, response)

    def handle_webhook(self, request):
        if request.method == "POST":
            # Verificar la firma del webhook
            if not self.verify_fb_token(request.headers.get("X-Hub-Signature"), request.data, self.fb_token):
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

