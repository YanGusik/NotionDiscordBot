import requests
import os
from dotenv import load_dotenv

load_dotenv()

# URL of the webhook
WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')
def send_embedded_message(title, url, fields, data):

    color = 2895667
    if (data['status'] == "Not started"):
        color = 2895667
    if (data['status'] == "In progress"):
            color = 2123412
    if (data['status'] == "Code review"):
            color = 7419530
    if (data['status'] == "On Test"):
            color = 15105570
    if (data['status'] == "Deploy"):
            color = 3447003
    if (data['status'] == "Done"):
            color = 5763719
    if (data['status'] == "Delayed"):
            color = 2303786

    # Create the embed object
    embed = {
        "title": title,
        "description": "The following information was extracted from the Notion database:",
        "url": url,
        "color": color,
        "fields": fields,
    }

    # Create the request payload
    data = {"embeds": [embed]}

    print("отправка")
    requests.post(WEBHOOK_URL, json=data)
    return
