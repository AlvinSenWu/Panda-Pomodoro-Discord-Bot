import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('welcome to {0.user} !'.format(client))


def timer(set_time):
    while set_time:
        mins = set_time
        print(mins, end="\r")
        time.sleep(1)
        set_time -= 1

@client.event
# checks messages if from the bot itself
async def on_message(message):
    if message.author == client.user:
      return
    

    # if user sends something to bot
    if message.content.startswith('-start'):
        await message.channel.send('Hello! starting the Pomodoro now!')
        set = await(message.channel.send('Enter the time in Minutes you would like:'))
        print(set)
      
        if message.content.startswith('-set'):
            timer(set)
            await message.channel.startswith('your time has been set to', set, '. Happy Studying!')
        
# running the bot with token


