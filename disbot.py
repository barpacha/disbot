import pyttsx3
import discord
import asyncio
TOKEN = 'NzMzMDA1MDYyNDQ3ODI1MDA3.Xw82KQ.nXIeG_Xievu-d6lcKr6Bq5Spjjo'

tts = pyttsx3.init()

bot = discord.Client()
@bot.event
async def on_message(message):
    if message.content[0] == '$':
        if message.author.voice is None or not bot.voice_clients is None:
            return
        lg = 'russian' if (message.content[1] < 'a' and message.content[1] > 'z') else 'english'
        voices = tts.getProperty('voices')
        for voice in voices:
            if voice.name == lg:
                tts.setProperty('voice', voice.id)
        voice = await message.author.voice.channel.connect(reconnect = True)
        if voice.is_connected():
            tts.save_to_file(message.content[1:], 'botsay.mp3')
            tts.runAndWait()
            voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg", source='botsay.mp3'), after=None)
            while voice.is_playing():
                await asyncio.sleep(1)
            await voice.disconnect()
        await message.edit(content=None)
    else:
        if message.content == 'stop' and not bot.voice_clients is None:
                voice = await message.author.voice.channel.connect(reconnect=True)
                voice.stop()
                await voice.disconnect()
bot.run(TOKEN)