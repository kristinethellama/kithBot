import discord
import os
import requests
import json
from awakeMe import keep_alive

client = discord.Client()

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
  if message.author == client.user:
    return

  if message.content.startswith('!compliment'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('!kiss'):
    msg = '*kisses* {0.author.mention}'.format(message)
    await message.channel.send(msg)



#Bot = commands.Bot(command_prefix="")

#@Bot.event
#  if "kiss" in message.content:
#    await Bot.send_message("kisses " + {client.user.name})

keep_alive()

client.run(os.getenv('TOKEN'))