# Messenger-to-Telegram-Bot
Un bot en Python que responde a mensajes de Facebook y ofrece notificaciones por Telegram usando sus APIs. Envía un mensaje al perfil de Facebook del bot para empezar. Incluye documentación y código de ejemplo. 
Aplicación de chatbot para Facebook Messenger y Telegram

Esta es una aplicación de chatbot que se integra con Facebook Messenger y Telegram para permitir a los usuarios interactuar con el bot y recibir respuestas automatizadas. La aplicación está escrita en Python y utiliza la biblioteca Flask para manejar solicitudes y respuestas HTTP.
Funciones del bot

El bot es capaz de realizar las siguientes funciones:

    Responder a los mensajes enviados por el usuario.
    Enviar una notificación a Telegram cuando un usuario está interesado en un trabajo.
    Proporcionar ayuda al usuario.

## Requisitos

    Python 3.6 o superior
    Pipenv para manejar las dependencias

## Configuración

Antes de ejecutar la aplicación, deberá seguir los siguientes pasos:

    Cree una cuenta de desarrollador en Facebook y Telegram para obtener los tokens de acceso necesarios.
    Clone este repositorio en su máquina local.
    Cree un archivo .env en la raíz del proyecto y defina las siguientes variables de entorno:


    FB_ACCESS_TOKEN=<su_token_de_acceso_de_facebook>
    FB_APP_SECRET=<su_clave_secreta_de_aplicacion_de_facebook>
    TELEGRAM_BOT_TOKEN=<su_token_de_acceso_de_telegram>
    TELEGRAM_CHAT_ID=<su_id_de_chat_de_telegram>

    Ejecute pipenv install en la raíz del proyecto para instalar las dependencias necesarias.
    Ejecute pipenv shell para activar el entorno virtual.
    Ejecute flask run para iniciar la aplicación.

## Uso

Una vez que la aplicación esté en funcionamiento, puede probar el bot enviando un mensaje a través de Facebook Messenger o Telegram. El bot responderá automáticamente a cualquier mensaje enviado por el usuario. Si un usuario escribe "estoy interesado", el bot enviará una notificación a Telegram y responderá con un mensaje agradeciendo al usuario por su interés. Si un usuario escribe "ayuda", el bot proporcionará información sobre cómo usar la aplicación.

## Contribuir

Si desea contribuir a este proyecto, puede enviar una solicitud de extracción con sus cambios propuestos. Antes de hacerlo, asegúrese de haber ejecutado las pruebas unitarias para garantizar que los cambios no rompan la aplicación existente.
