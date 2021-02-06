import fileManager
import discord
import MsgParser
import asyncio
import Talker
import parametrs
import random

def append_handler(parser:MsgParser.MsgParser):
    async def stop(bot, message):
        bot.playing[message.author.voice.channel.id] = None
        await message.delete()
    parser.add_handler(stop, 'stop')

    async def voices(bot, message):
        voices = Talker.Talker(parametrs.Talker()).get_voices()
        text = ''
        for i in voices:
            text += i + '\n'
        await bot.send(message.channel, text, delete_after=180)
        await message.delete()
    parser.add_handler(voices, 'voices')

    async def off(bot, message):
        if message.author.name == 'barpacha':
            await bot.logout()
            print('logout')
    parser.add_handler(off, 'off')

    async def help(bot, message):
        text = '$ перед воспроизводимым сообщением\nтег - [название значение]\nтеги:\nv - Громкость\np - высота голоса\ns - скорость воспроизведения\nch - канал\nvc - голос\nf - воспроизведение файла\n\nкоманды:\nvoices - голоса\nsaved - сохраненные записи\nstop - прекратить воспроизведение\n\nдля добавления записей необходимо отправить файл mp3/wav в личку боту, в комментариях к файлу указать имя записи.'
        await bot.send(message.channel, text, delete_after=300)
        await message.delete()
    parser.add_handler(help, 'help')

    async def ping(bot, message):
        await bot.send(message.channel, random.randint(0, 1000).__str__(), delete_after=300)
        await asyncio.sleep(300)
        await message.delete()
    parser.add_handler(ping, 'ping')
    parser.add_handler(ping, '<:ping:798579897726926938>')

    async def saved(bot, message):
        saved = fileManager.all_files()
        text = ''
        for i in saved:
            text += i + '\n'
        await bot.send(message.channel, text, delete_after=180)
        await message.delete()
    parser.add_handler(saved, 'saved')

    async def kazino(bot, message):
        if random.randint(0, 3) == 1:
            await bot.send(message.channel, 'вы выиграли', delete_after=180)
        else:
            await bot.send(message.channel, 'вы проиграли', delete_after=180)
        await asyncio.sleep(180)
        await message.delete()
    parser.add_handler(kazino, 'казино')

    async def bagoga(bot, message):
        message.content = r'$[f бажожда]'
        await default_handler(bot, message)
    parser.add_handler(bagoga, '<:bazozda:803347064904876072>')

    async def test(bot, message):
        await message.delete()
        message = await bot.wait_msg(message.author,60)
        print(message.content)
    parser.add_handler(test, 'test')

    async def fast_f(bot, message):
        await message.delete()
        message = await bot.wait_msg(message.author,120)
        message.content = r'$[f ' + message.content  + ']'
        await default_handler(bot, message)
    parser.add_handler(fast_f, 'f')

    return parser

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
        m = append_handler(m)
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




