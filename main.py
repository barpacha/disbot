import DiscordApi
import asyncio
import discord_command
import os
import sys

async def main():
    bot = DiscordApi.MyClient('TOKEN', discord_command.default_handler)
    await bot.start()
    print('ready')
    while True:
        await asyncio.sleep(1000)

asyncio.run(main())