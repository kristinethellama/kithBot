import discord
import os
import requests
import json
from awakeMe import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

bot = Bot(command_prefix='!')

def __init__(self):
  self.bot = discord.Client()

# random compliment generator
def get_quote():
  response = requests.get("https://complimentr.com/api")
  json_data = json.loads(response.text)
  quote = json_data["compliment"]
  return(quote)

@bot.command(name='server', help = 'Fetches server information')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')
	await context.send(f'Server Name: {guild.owner.display_name}')


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  await client.change_presence(activity=discord.Game('!help'))    
  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
  # make sure msgs are diff from user and bot prevent spammies
  if message.author == client.user:
    return

  # random compliment generator
  if message.content.startswith('!compliment'):
    quote = get_quote()
    await message.channel.send(quote)
  
  # lists commands
  if message.content.startswith('!help'):
    await message.channel.send('```i am kith bot! your simple wholesome bot! ❤️```')
    await message.channel.send('```my commands are simple: !kiss sends you a kiss, !hug sends you a hug, and !compliment will give you a cute compliment!! 🐸💕```')

  # command to make bot kissy
  if message.content.startswith('!kiss'):
    mention = message.author.mention
    response = f"**kisses** {mention}"
    await message.channel.send(response)
    await message.channel.send(file=discord.File('img/bunnykiss.gif'))
  
  # command to make bot huggies
  if message.content.startswith('!hug'):
    mention = message.author.mention
    response = f"**hugs** {mention}"
    await message.channel.send(response)  
    await message.channel.send(file=discord.File('img/cathug.gif')) 

# function to allow bot to run on repl webserver
keep_alive()

client.run(os.getenv('TOKEN'))