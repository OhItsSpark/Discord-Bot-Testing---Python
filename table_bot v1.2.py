import discord # Imports Discord
import requests
import json
import random, os

# Creates def get_meme, proceeds to import from meme-api and uses return to read the https request
def get_meme(): 
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# Creates def get_me_pomnies, uses random and os to send the pomni image, os is used to interact with my operating system
def get_me_pomnies(): 
    pomnis = os.listdir('images/pomnis')

    selected_pomnis = random.choice(pomnis)
    files = [discord.File(f'images/pomnis/{selected_pomnis}')]
    
    return files

# This allows to communicate with Discord, used to assign commands to the bot

class MyClient(discord.Client): 
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) # Will tell you who are you logged as [Discord bot]
    async def on_message(self, message):
        if message.author == self.user:
            return
        # Will tell you options
        if message.content.startswith('options'):
            await message.channel.send("For options you can use:\n" \
            "1.- **hello**\n" \
            "2.- **send me a meme**\n" \
            "3.- **easter_egg**\n"
            "4.- **send me pomni**\n"
            "5.- **send me a pomni**\n"
                                       )
        # Will say hello back
        if message.content.startswith('hello'):
            await message.channel.send("Hello & welcome")
        
        # Will send you a random reddit meme
        if message.content.startswith('send me a meme'):
            await message.channel.send(get_meme())

        # Will rick roll you
        if message.content.startswith('easter_egg'):
            await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ') # Mwhehehehe

        # Will send you pmni
        if message.content.startswith('send me pomni'):
            await message.channel.send(file=discord.File('images/pomni.jpg'))

        # Will randomly send you a pomni
        if message.content.startswith('send me a pomni'):
            await message.channel.send(files=get_me_pomnies())



intents = discord.Intents.default()
intents.message_content = True

# Put your Discord token here

client = MyClient(intents=intents)
client.run('[TOKEN]')
