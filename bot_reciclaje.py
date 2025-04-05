# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import os
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def mem(ctx):
    meme = random.choice(os.listdir("imagenes"))

    with open(f'imagenes/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    meme = random.choice(os.listdir("Memes de reciclaje"))

    with open(f'Memes de reciclaje/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 

@bot.command()
async def datos(ctx):
    lista = ["la contaminación del aire ambiente (exterior) en las ciudades y zonas rurales de todo el mundo provoca cada año 4,2 millones de muertes prematura",
             "Son terribles para la salud humana",
             "La contaminación ambiental es la presencia de componentes nocivos, bien sean de naturaleza biológica, química o de otra clase, en el medioambiente, de modo que supongan un perjuicio para los seres vivos que habitan un espacio, incluyendo, por supuesto, a los seres humanos"]
    await ctx.send(random.choice(lista))        
    
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run('Tokken')
