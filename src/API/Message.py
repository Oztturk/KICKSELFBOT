import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send(contetn):

    auth_token = os.getenv('KICK_AUTH_TOKEN')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': 'application/json',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://dashboard.kick.com/',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}',
        'Origin': 'https://dashboard.kick.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    json_data = {
        'content': contetn,
        'type':'message'
    }

    requests.post('https://kick.com/api/v2/messages/send/22070259', headers=headers, json=json_data)
