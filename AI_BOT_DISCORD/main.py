import discord
from discord.ext import commands
from ai_logic import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./images/{file_name}")
        await ctx.send(get_class(file_name))    
    else:
        await ctx.send("Картинки не найдены")        
    

bot.run("")    