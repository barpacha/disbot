import DiscordApi
import asyncio
import discord_command
import os
import sys

async def main():
    bot = DiscordApi.MyClient('NzMzMDA1MDYyNDQ3ODI1MDA3.Xw82KQ.Ef0e_FTtMaUwBFAYIR1dwsw8Bgk', discord_command.default_handler)
    await bot.start()
    print('ready')
    while True:
        await asyncio.sleep(1000)

asyncio.run(main())