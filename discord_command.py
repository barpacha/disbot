import fileManager
import discord
import MsgParser
import asyncio
import Talker
import parametrs
import random

async def stop(bot, message):
    bot.playing[message.author.voice.channel.id] = None

async def voices(bot, message):
    voices = Talker.Talker(parametrs.Talker()).get_voices()
    text = ''
    for i in voices:
        text += i + '\n'
    await bot.send(message.channel, text, delete_after=180)
    await message.delete()

async def off(bot, message):
    if message.author.name == 'barpacha':
        await bot.logout()
        print('logout')

async def help(bot, message):
    text = '$ перед воспроизводимым сообщением\nтег - [название значение]\nтеги:\nv - Громкость\np - высота голоса\ns - скорость воспроизведения\nch - канал\nvc - голос\nf - воспроизведение файла\n\nкоманды:\nvoices - голоса\nsaved - сохраненные записи\nstop - прекратить воспроизведение\n\nдля добавления записей необходимо отправить файл mp3/wav в личку боту, в комментариях к файлу указать имя записи.'
    await bot.send(message.channel, text, delete_after=300)
    await message.delete()

async def ping(bot, message):
    await bot.send(message.channel, random.randint(0,1000).__str__(), delete_after=300)
    await asyncio.sleep(300)
    await message.delete()

async def saved(bot, message):
    saved = fileManager.all_files()
    text = ''
    for i in saved:
        text += i + '\n'
    await bot.send(message.channel, text, delete_after=180)
    await message.delete()

async def kazino(bot, message):
    if random.randint(0, 1)==1:
        await bot.send(message.channel, 'вы выиграли', delete_after=180)
    else:
        await bot.send(message.channel, 'вы проиграли', delete_after=180)
    await asyncio.sleep(180)
    await message.delete()

async def bagoga(bot, message):
    message.content = r'$[f бажожда]'
    await default_handler(bot, message)

async def default_handler(bot, message):
    if message.content == '':
        return
    if message.channel.type == discord.ChannelType.private:
        if len(message.attachments) == 0:
            return
        if fileManager.download(message.attachments[0].url, message.content):
            await bot.send(message.channel, 'готово', delete_after=None)
        else:
            await bot.send(message.channel, 'имя занято', delete_after=None)
    else:
        m = MsgParser.MsgParser(message, bot)
        if not m.is_talk:
            return
        if message.author.voice is None and m.channel is None:
            return
        for f in m.file_mas:
            if m.channel is None:
                channel = message.author.voice.channel
            else:
                channel = m.channel
            await bot.append_playlist(channel, f)
        await message.delete()




