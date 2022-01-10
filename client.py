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
    global pause, stop, canPause, canStop
    global seconds

    

    if message.author == client.user:
      return
      
    # starting the bot by giving instructions
    if message.content.startswith('-start'):
        await message.channel.send('Hello! Welcome the Pomodoro now!')
        await message.channel.send('For list of commands type -c ')


    # command pallete
    if message.content.startswith('-c'):
        await message.channel.send('The list of comamnds include:')
        await message.channel.send('-set [enter time in minutes] to set the time you would like to set your session time to')
        await message.channel.send('-p to pause your session')
        await message.channel.send('-r to pause your session')
        await message.channel.send('-t to terminate your session')
        
        
    if message.content.startswith('-set'):
        total_sec = int(message.content.split(' ')[1])*60
        secString = total_sec
        seconds = total_sec
        timeR_msg = await message.channel.send(embed = discord.Embed(
            title = 'Panda Pomodoro session has started!\nYour time has been set to{:2d}\nHappy studying!\nTime remaining: {:02d}:00'.format(total_sec//60, total_sec//60),
            colour = discord.Colour.teal(),
        ).set_image(url = 'https://cdn.shopify.com/s/files/1/0212/4909/7828/products/DynamicImageHandler_3c06c2f3-2b1d-4445-9d92-217e5d27bfa0.png?v=1589733581'))
        pause, stop = False, False
        canPause, canStop = True, True
        while not pause and not stop and total_sec:
            time.sleep(1)
            total_sec-=1
            seconds-=1
            await timeR_msg.edit(embed=discord.Embed(
                title='Panda Pomodoro session has started!\nYour time has been set to '+ str(secString//60) +'\nHappy studying!\nTime remaining: ' + clock.desc(total_sec),
                colour = discord.Colour.teal(),
            ).set_image(url = 'https://cdn.shopify.com/s/files/1/0212/4909/7828/products/DynamicImageHandler_3c06c2f3-2b1d-4445-9d92-217e5d27bfa0.png?v=1589733581'))

    if message.content.startswith('-r'):
        try:
            if pause:
                total_sec = seconds
                secString = total_sec
                timeR_msg = await message.channel.send(
                    embed = discord.Embed(
                        title = 'Panda Pomodoro session has resumed!\nResuming session at {:02d}:{:02d}\nTime remaining: {:02d}:{:02d}'.format(secString//60, secString%60, total_sec//60, total_sec%60),
                        colour = discord.Colour.teal(),
                    ).set_image(url = 'https://cdn.shopify.com/s/files/1/0212/4909/7828/products/DynamicImageHandler_3c06c2f3-2b1d-4445-9d92-217e5d27bfa0.png?v=1589733581')
                )
                pause = False
                canPause, canStop = True, True
                while not pause and total_sec:
                    time.sleep(1)
                    total_sec-=1
                    seconds-=1
                    await timeR_msg.edit(
                        embed = discord.Embed(
                            title = 'Panda Pomodoro session has resumed!\nResuming session at {:02d}:{:02d}\nTime remaining: {:02d}:{:02d}'.format(secString//60, secString%60, total_sec//60, total_sec%60),
                            colour = discord.Colour.teal(),
                        ).set_image(url = 'https://cdn.shopify.com/s/files/1/0212/4909/7828/products/DynamicImageHandler_3c06c2f3-2b1d-4445-9d92-217e5d27bfa0.png?v=1589733581')
                    )

            elif stop:
                await message.channel.send('There is no session to resume')
            else:
                await message.channel.send('Your session has not been paused')
        except NameError:
            await message.channel.send('There is no session to resume')
            
    if message.content.startswith('-p'):
        pause = True
        try:
            if canPause:
                canPause = False
                total_sec = seconds
                await message.channel.send('Your session has been paused')
                await message.channel.send('Type -r to resume your session')
            else:
                await message.channel.send('You cannot pause')
        except NameError:
            await message.channel.send('You have no session to pause')

    
    if message.content.startswith('-t'):
        stop = True
        try:
            if canStop:
                pause, canPause, canStop = False, False, False
                total_sec = 0
                await message.channel.send('You have terminated your current senssion.')
                await message.channel.send('-set [enter time in minutes] to set a new session')
            else:
                await message.channel.send('You have no session to terminate')
        except NameError:
            await message.channel.send('You have no session to terminate')

        


# running the bot with token
# print(os.environ.get('TOKEN'))
client.run(os.environ.get('TOKEN'))
# client.run('TOKEN')
