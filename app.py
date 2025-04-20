from flask import Flask, request, abort
import requests

import os
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")


app = Flask(__name__)

@app.route('/pushover-webhook', methods=['POST'])
def pushover_webhook():
    if not request.form:
        abort(400)

    titre = request.form.get('title', 'Notification Pushover')
    message = request.form.get('message', 'Aucun message')

    discord_data = {
        "content": f"📩 **{titre}**\n{message}"
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=discord_data)

    if response.status_code == 204:
        return '', 204
    else:
        print("Erreur Discord :", response.text)
        return 'Erreur Discord', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
