# bot.py
import os
import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

colorschemes = ['java', 'c++', 'python', 'js', 'css', 'html', 'assembly']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '-cs' in message.content[:3]:
        print(f'REQUEST: {message.content}')
        await message.channel.send('I AM SOMEWHAT READY')
        r = requests.get('https://cheat.sh/' + message.content[4:].replace(' ', '+') + '?TQ')
        print(f'RESPONSE: {r.text}')
        lang = ''
        for l in colorschemes:
            if l in message.content:
                lang = l
                break

        if len(r.text) != 0:
            await message.channel.send('```' + lang + r.text[:1998] + '```')
        else:
            await message.channel.send('SORRY. NOT FOUND')



client.run(TOKEN)

