import sys
sys.dont_write_bytecode = True

import asyncio

from .API.Auth import GetUserId
from .Websocket.ws import listen
from src.Commands import load_commands
from src.Classes import Command
from dotenv import load_dotenv
import os
load_dotenv()

async def main():
     username = os.getenv('CHANNEL_NAME')

     user_id = GetUserId(username)
     channel_name = f'private-channel_{user_id}'
     load_commands()
     await listen(username, channel_name)


if __name__ == '__main__':
     asyncio.run(main())
