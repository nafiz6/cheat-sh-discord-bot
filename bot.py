# bot.py
import os
import requests
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

colorschemes = ['java', 'c++', 'python', 'js', 'css', 'html', 'assembly', 'javascript']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '-cs' in message.content[:3]:
        print(f'REQUEST: {message.content}')
        r = requests.get('https://cheat.sh/' + message.content[4:].replace(' ', '+') + '?TQ')
        resWithText = requests.get('https://cheat.sh/' + message.content[4:].replace(' ', '+') + '?T')
        print(f'RESPONSE: {r.text}')
        lang = ''
        lowerCaseContent = message.content.lower()
        for l in colorschemes:
            if l in lowerCaseContent:
                print(f'language: {l}')
                lang = l
                break
        stackoverflow = re.search(r'\[so/q/.*?\]', resWithText.text)


        if len(r.text) != 0:
            if len(r.text) < 1000:
                await message.channel.send('```' + lang + '\n'+ resWithText.text + '```')
            else:
                await message.channel.send('```' + lang + '\n'+ r.text[:1900] + '```')
            if stackoverflow:
                match = stackoverflow.group(0)
                msg = match[6: len(match) - 1]
                await message.channel.send('https://stackoverflow.com/questions/' + msg)
        else:
            await message.channel.send('SORRY. NOT FOUND')



client.run(TOKEN)

