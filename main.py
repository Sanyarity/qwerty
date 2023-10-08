import discord
from bot_logic import gen_pass 
from game import flip_coin
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

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, lenght = 10):
    await ctx.send(gen_pass(lenght))

@bot.command()
async def flip_coin(ctx):
    await ctx.send(flip_coin())


@bot.command()
async def mem(ctx):
    with open(f'discord3/images{mem}', 'rb') as f:
            picture = discord.File(f)  
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_animal_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
@bot.command('duck')
async def animal(ctx):
    image_url = get_animal_image_url()
    await ctx.send(image_url)    
bot.run("MTE1MjkwMzI0OTAyMDU5MjE3OQ.Gnsca-.GnNVIHKV_nkvVNrSmS-c55XS-5aZkv_PFbL6SQ")