import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "Что такое глобальное потепление?":
        await message.channel.send("Глобальное потепление — это постепенное повышение температуры на Земле")
    if message.content == "Теория":
        await message.channel.send("https://www.youtube.com/watch?v=ynqAe4nl-QI&pp=ygUp0JPQu9C-0LHQsNC70YzQvdC-0LUg0L_QvtGC0LXQv9C70LXQvdC40LU%3D") 
    elif message.content == "Статья":
        await message.channel.send("https://tass.ru/spec/climate")
    elif message.content == "Help":
        await message.channel.send("Теория - отправляет видео о глобальном потеплении")
    elif message.content == "Help":
        await message.channel.send("Что такое глобальное потепление? - показывает о том что такое глобальное потепление")
    
    else:
        await message.channel.send(message.content)






bot.run("")    
