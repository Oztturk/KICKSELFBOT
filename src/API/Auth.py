import primp
import os
import requests.exceptions  # Hata yakalama için hala gerekli
from dotenv import load_dotenv

load_dotenv()

def GetUserId(username):
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': '*/*',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=0',
    }

    response = primp.get(f'https://kick.com/api/v2/channels/{username}', headers=headers)
    return response.json().get("id")

async def getAuthToken(username,socketid):
    auth_token = os.getenv('KICK_AUTH_TOKEN')
    if not auth_token:
        return None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
        'Accept': 'application/json',
        'Referer': 'https://dashboard.kick.com/',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {auth_token}',
        'Origin': 'https://dashboard.kick.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Mode': 'cors',
    }

    if not socketid:
        return None

    json_data = {
        "socket_id": socketid,
        'channel_name': f'private-channel_{GetUserId(username)}',
    }

    try:
        response = primp.post('https://kick.com/broadcasting/auth', headers=headers, json=json_data)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"İstek sırasında bir hata oluştu: {e}")
        return None
