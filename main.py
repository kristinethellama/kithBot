import discord
import os
import requests
import json
from awakeMe import keep_alive
from discord.ext import commands

client = discord.Client()

def __init__(self):
  self.bot = discord.Client()

# random compliment generator
def get_quote():
  response = requests.get("https://complimentr.com/api")
  json_data = json.loads(response.text)
  quote = json_data["compliment"]
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  # make sure msgs are diff from user and bot prevent spammies
  if message.author == client.user:
    return

  # random compliment generator
  if message.content.startswith('!compliment'):
    quote = get_quote()
    await message.channel.send(quote)

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