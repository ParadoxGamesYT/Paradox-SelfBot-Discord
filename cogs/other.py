import os

try:
    import random
except: os.system('pip install random')

try:
    import discord
except: os.system('pip install discord')

from discord.ext import commands

try:
    from colorama import Fore, init
except: pass

init()

class other(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def popit(self, ctx):
        """поп ит"""
        await ctx.send('''||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||''')

    @commands.command()
    async def ball(self, ctx, *, arg=None):
        if arg == None:
            message = await ctx.send('**Ты не задал вопрос**')
            await message.add_reaction('❌')
        else:
            env = ["Спроси позже","можешь быть уверен в этом", "мне кажется нет",]
            rch = random.choice(env)
            await ctx.send(f'**{arg}** - {rch}')

    @commands.command()
    async def reactionall(self, ctx, count: int=50, reaction: discord.Emoji=None):
        await ctx.message.delete()
        if reaction == None:
            mess = await ctx.send('**Ты не указал эмодзи**')
            await mess.add_reaction('❌')
        else:
            messages = await ctx.channel.history(limit=count).flatten()
            reacted = 0
            for message in messages:
                await message.add_reaction()
                reacted += 1
            await ctx.send(f'**Поставлены реакции под {reacted} сообщениями**')
  
            
def setup(client):
    client.add_cog(other(client))