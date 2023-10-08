import discord
from discord.ext import commands
import os
from random import choice
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


mems = os.listdir("discord3/images")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command('no_trash')
async def no_trash(ctx):
    url = 'https://www.youtube.com/watch?v=X20jkp44KmQ'
    await ctx.send(url)

bot.run("")