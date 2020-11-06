import subprocess
import discord
import asyncio
TOKEN = 'NzMzMDA1MDYyNDQ3ODI1MDA3.Xw82KQ.nXIeG_Xievu-d6lcKr6Bq5Spjjo'

bot = discord.Client()
@bot.event
async def on_message(message):
    if message.content[0] == '$':
        if message.author.voice is None:
            return
        voice = await message.author.voice.channel.connect(reconnect = True)
        if voice.is_connected():
            subprocess.Popen(['balcon.exe', '-n', 'Microsoft Irina Desktop', '-t', message.content[1:], '-w','botsay.mp3']).wait()
            voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg", source='botsay.mp3'), after=None)
            while voice.is_playing():
                await asyncio.sleep(1)
            await voice.disconnect()
            await message.delete()
    else:
        if message.content == 'stop' and not bot.voice_clients is None:
            voice = await message.author.voice.channel.connect(reconnect=True)
            voice.stop()
            await voice.disconnect()
            await message.delete()
bot.run(TOKEN)