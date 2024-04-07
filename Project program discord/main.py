import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif await message.channel.startwish("$Что такое глобальное потепление"):
        await message.channel.send("Глобальное потепление — это постепенное повышение температуры на Земле")
     
    else:
        await message.channel.send(message.content)






bot.run("")    
