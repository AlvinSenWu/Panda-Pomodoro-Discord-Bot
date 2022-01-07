import discord
import time
import os

client = discord.Client()

@client.event
async def on_ready():
    print('welcome to {0.user} !'.format(client))


def timer(set_time):
    set_time = set_time*60
    while set_time:
        mins, secs = divmod(set_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
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
        await message.channel.send('Enter the time in Minutes you would like:') 
        # set = await(message.channel.send('Enter the time in Minutes you would like:'))
        # print(set)
        
    if message.content.startswith('-set'):
        # timer(set)
        # set = await(message.channel.send('Enter the time in Minutes you would like:'))
        set = int(message.content.split(' ')[1])
        await message.channel.send('your time has been set to ' + str(set) + ' Happy Studying!')
        timer(set)
        
# running the bot with token

