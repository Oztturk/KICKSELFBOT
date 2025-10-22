import asyncio
import websockets
import json
from ..API.Auth import getAuthToken
from ..API.Message import send
from ..Classes import Command
from dotenv import load_dotenv
from ..config import CONSTANTS
import os
load_dotenv()


WEBSOCKET_URL = "wss://ws-us2.pusher.com/app/32cbd69e4b950bf97679?protocol=7&client=js&version=8.4.0&flash=false"

async def listen(username: str, channel_name: str):

    try:
        async with websockets.connect(WEBSOCKET_URL) as websocket:

            connection_msg = await websocket.recv()
            connection_data = json.loads(connection_msg)
            if connection_data.get("event") != "pusher:connection_established":

                return

            socket_id_data = json.loads(connection_data["data"])
            socket_id = socket_id_data.get("socket_id")

            auth_response = await getAuthToken(username, socket_id)
            if not auth_response or "auth" not in auth_response:
                return
            auth_key = auth_response["auth"]

            subscribe_message = {
                "event": "pusher:subscribe",
                "data": {
                    "auth": auth_key,
                    "channel": channel_name
                }
            }
            chat_sub = {"event":"pusher:subscribe","data":{"auth":"","channel":"chatrooms.22070259.v2"}}
            await websocket.send(json.dumps(subscribe_message))
            await websocket.send(json.dumps(chat_sub))
            print("Connected to web sockets")
            while True:
                message = await websocket.recv()
                data = json.loads(message)


                if data.get("event") == "App\Events\ChatMessageEvent":
                    print(data)
                    message_data = json.loads(data["data"])
                    message_content = message_data.get("content")
                    sender = message_data.get("sender").get("username")


                    if message_content == "[emote:37232:PeepoClap]" and sender != os.getenv('CHANNEL_NAME'):
                        send("[emote:37232:PeepoClap]")

                    else:
                        if not Command.run(message_content.lower(), sender=sender):
                            print(f"Bilinmeyen komut veya komut değil: {sender}: {message_content}")





                if data.get("event") == "FollowerDeleted":
                    try:
                        follower_data = json.loads(data["data"])
                        follower_slug = follower_data.get("user", {}).get("slug")
                        follower_username = follower_data.get("user", {}).get("username")

                        if follower_slug:
                            message_to_send = f"@{follower_username} {CONSTANTS['UNFOLLOW_MESSAGE']}"
                            send(message_to_send)
                    except json.JSONDecodeError:
                        print("0x1")

                if data.get("event") == "FollowerAdded" and data.get("data"):
                    try:
                        follower_data = json.loads(data["data"])
                        follower_slug = follower_data.get("user", {}).get("slug")
                        follower_username = follower_data.get("user", {}).get("username")

                        if follower_slug:
                            message_to_send = f"@{follower_username} {CONSTANTS['NEW_FOLLOWER_MESSAGE']}"
                            send(message_to_send)
                    except json.JSONDecodeError:
                        print("0x1")

                if data.get("event") == "pusher:ping":
                    await websocket.send(json.dumps({"event": "pusher:pong", "data": {}}))
                    print("ponged")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"WebSocket bağlantısı kapandı: {e}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
