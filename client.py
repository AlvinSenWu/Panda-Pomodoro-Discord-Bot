import discord
import time
import os
from discord.colour import Colour
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
    
    style = discord.Embed(
        title = 'Panda Pomodoro session has started!',
        colour = discord.Colour.teal(),
        )

    style.set_image(url = 'https://cdn.shopify.com/s/files/1/0212/4909/7828/products/DynamicImageHandler_3c06c2f3-2b1d-4445-9d92-217e5d27bfa0.png?v=1589733581')


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
        await message.channel.send('-r to pause your session')
        await message.channel.send('-t to terminate your session')
        
    if message.content.startswith('-set'):
        await message.channel.send(embed = style)
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
            
    
    if message.content.startswith('-p'):
        pause = True
        total_sec = seconds
        # this line only works first pause: await message.channel.send('you have paused your session at {:02d}:{:02d}'.format(total_sec//60, total_sec%60))
        await message.channel.send('Your session has been paused')
        await message.channel.send('Type -r to pause your session')

    
    if message.content.startswith('-t'):
        pause = True
        total_sec = 0 # need to somehow make the time be 0 when terminated, so it cannot be resumed. if impleneted like this, needs to be seperate if statement
        await message.channel.send('You have terminated your current senssion.')
        await message.channel.send('-set [enter time in minutes] to set a new session')

# BUGS:
# -p only pauses once and uses that time for all future resumes
# -r can be used while session is already in place
        



# running the bot with token
# print(os.environ.get('TOKEN'))
# client.run(os.environ.get('TOKEN'))
client.run('TOKEN')