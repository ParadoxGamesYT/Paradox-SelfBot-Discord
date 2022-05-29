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

init()

class status(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def stream(self, ctx, *, arg='Deadons — https://t.me/deadons'):
        await ctx.message.delete()
        await self.client.change_presence(activity=discord.Streaming(name=arg, url='https://twitch.tv/404%27'))
        messsge = await ctx.send(f'**Готово**')
        await messsge.add_reaction('✅')
            
    @commands.command()
    async def competing(self, ctx, *, arg='Deadons — https://t.me/deadons'):
        await ctx.message.delete()
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name=arg, type=discord.ActivityType.competing))
        messsge = await ctx.send(f'**Готово**')
        await messsge.add_reaction('✅')
            
    @commands.command()
    async def play_status(self, ctx, *, arg='Deadons — https://t.me/deadons'):
        await ctx.message.delete()
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=arg))
        messsge = await ctx.send(f'**Готово**')
        await messsge.add_reaction('✅')
            
    @commands.command()
    async def listen(self, ctx, *, arg='Deadons — https://t.me/deadons'):
        await ctx.message.delete()
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
        messsge = await ctx.send(f'**Готово**')
        await messsge.add_reaction('✅')

    @commands.command()
    async def watch(self, ctx, *, arg='Deadons — https://t.me/deadons'):
        await ctx.message.delete()
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name=arg, type=discord.ActivityType.watching))
        messsge = await ctx.send(f'**Готово**')
        await messsge.add_reaction('✅')
            

def setup(client):
    client.add_cog(status(client))