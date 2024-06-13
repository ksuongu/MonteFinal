#import class libraries needed
import discord
import random
import os
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

#output to check if imported class library is functioning
print('this is',  ec2_metadata.region)
print('this is',  ec2_metadata.instance_id)
load_dotenv()

#create client and object, add intents of bot
intents = discord.Intents.default()
intents.message_content = True; #have bot read messaage
client = discord.Client(intents = intents)
token = str(os.getenv('TOKEN'))

# Initialize bot
@client.event
async def on_ready():
    print(f"Logged in as bot {client.user}")

# Setting simple bot responses to key phrases

#getting data from test server
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content).lower()

    # Print test for server
    print(f'Message "{user_message}" by {username} on {channel}')

    # Bot responses to key phrases
    if channel == "bot-test":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "pooty":
            await message.channel.send('hehe pooty')
        elif user_message.lower() == "need a dance move":
            dance_moves = ["hip twist", "crab walk", "ball and chain", "pike", "body thread", "master swipe"];
            await message.channel.send(random.choice(dance_moves))

client.run(token)
