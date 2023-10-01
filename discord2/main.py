import discord
from bot_logic import gen_pass 
from game import flip_coin
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

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
bot.run("MTE1MjkwMzI0OTAyMDU5MjE3OQ.GlvPdk.9hcqCoGrfjsEPIlr7oE3IDZaSjWiZI6Byf0zNw")