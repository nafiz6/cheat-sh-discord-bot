# bot.py
import os
import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(f'message received {message}')
    if message.author == client.user:
        return

    if '-cs' in message.content[:3]:
        print(f'REQUEST: {message.content}')
        await message.channel.send('I AM NOT READY YET')
        r = requests.get('https://cheat.sh/' + message.content[4:].replace(' ', '+') + '?TQ')
        print(f'RESPONSE: {r.text}')

        await message.channel.send(r.text[:1998])



client.run(TOKEN)

