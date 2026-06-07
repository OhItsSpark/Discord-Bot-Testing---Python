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

# Creates deg_get_me_ragathas, searches in folder images/ragathas in order to obtain a random image to send to Discord

def get_me_ragathas():
    ragathas = os.listdir('images/ragathas')

    selected_ragathas = random.choice(ragathas)
    files = [discord.File(f'images/ragathas/{selected_ragathas}')]

    return files

# Same as before but with Jax

def get_me_jaxes():
    jaxes = os.listdir('images/jaxes')

    selected_jaxes = random.choice(jaxes)
    files = [discord.File(f'images/jaxes/{selected_jaxes}')]
    
    return files

# This allows to communicate with Discord, used to assign commands to the bot

class MyClient(discord.Client): 
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user)) # Will tell you who are you logged as [Discord bot]
    async def on_message(self, message):
        if message.author == self.user:
            return
        # Will tell you options
        if message.content.startswith('help'):
            await message.channel.send("For options you can use:\n" \
            "1.- **hello**\n" \
            "2.- **send me a meme** - it will send you a random meme from the internet\n"\
            "3.- **easter egg**\n"
            "4.- **send me pomni** - it will send you a specific pomni\n"
            "5.- **send me a pomni** - it will send you a pomni\n"
            "6.- **send me a ragatha** - it will send you a ragatha\n"
            "7.- **send me a jax** - it will send you a jax\n"
            "8.- **felix.txt** - txt file of felix the cat\n"
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

        # Will send you pomni
        if message.content.startswith('send me pomni'):
            await message.channel.send(file=discord.File('images/pomni.jpg'))

        # Will send you a txt file of felix the cat

        if message.content.startswith('felix.txt'):
            await message.channel.send(file=discord.File('files/felix.txt'))

        # Will randomly send you a pomni
        if message.content.startswith('send me a pomni'):
            await message.channel.send(files=get_me_pomnies())

        # Will provide you a random ragatha
        if message.content.startswith('send me a ragatha'):
            await message.channel.send(files=get_me_ragathas())

        # Will provide a random jax
        if message.content.startswith('send me a jax'):
            await message.channel.send(files=get_me_jaxes())



intents = discord.Intents.default()
intents.message_content = True

# Put your token here

client = MyClient(intents=intents)
client.run('[TOKEN]')
