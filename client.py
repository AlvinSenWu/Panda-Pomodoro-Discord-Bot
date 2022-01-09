import discord
import time
import os
from clock import Clock


client = discord.Client()

@client.event
async def on_ready():
    print('welcome to {0.user}!'.format(client))


@client.event
# checks messages if from the bot itself
async def on_message(message):
    clock = Clock()
    global pause
    global stop
    global seconds
    
    if message.author == client.user:
      return
      
    # starting the bot by giving instructions
    if message.content.startswith('-start'):
        await message.channel.send('Hello! starting the Pomodoro now!')
        await message.channel.send('For list of commands type -c ')
        # await message.channel.send('Enter the time in Minutes you would like:') 

    # command pallete
    if message.content.startswith('-c'):
        await message.channel.send('The list of comamnds include:')
        await message.channel.send('-set [enter time in minutes] to set the time you would like to set your session time to')
        await message.channel.send('-p to pause your session')
        
    if message.content.startswith('-set'):
        total_sec = int(message.content.split(' ')[1])*60
        seconds = total_sec
        await message.channel.send('Your time has been set to ' + str(total_sec//60) + ' minutes. Happy Studying!')
        timeR_msg = await message.channel.send('Time remaining: {:02d}:00'.format(total_sec//60))
        pause = False
        while not pause:
            time.sleep(1)
            total_sec-=1
            seconds-=1
            await timeR_msg.edit(content='Time remaining: ' + clock.desc(total_sec))

    if message.content.startswith('-r'):
        total_sec = seconds
        await message.channel.send('Resuming session at {:02d}:{:02d}'.format(total_sec//60, total_sec%60))
        timeR_msg = await message.channel.send('Time remaining: {:02d}:{:02d}'.format(total_sec//60, total_sec%60))
        pause = False
        while not pause:
            time.sleep(1)
            total_sec-=1
            await timeR_msg.edit(content='Time remaining: ' + clock.desc(total_sec))
            
    
    if message.content.startswith('-stop') or message.content.startswith('-p'):
        pause = True
        if message.content.startswith('-stop'):
            await message.channel.send('You have stopped your current senssion.')
            await message.channel.send('-set [enter time in minutes] to set a new session')

# running the bot with token
# print(os.environ.get('TOKEN'))
# client.run(os.environ.get('TOKEN'))
client.run('token')
