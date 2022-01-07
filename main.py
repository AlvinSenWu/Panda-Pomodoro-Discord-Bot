import discord
import time
import os

client = discord.Client()

class Param:
    def __init__(self):
        self.mins = 0
        self.secs = 0

@client.event
async def on_ready():
    print('welcome to {0.user}!'.format(client))

async def timer(min, sec, message, pause=False):
    # set_time = set_time*60
    # 
    # mins = 0
    # secs = 0
    set_time = min*60
    msg = await message.channel.send('{:02d}:00'.format(min))
    mins = 0
    secs = 0
    while set_time:
        if not pause:
            # mins, secs = divmod(set_time, 60)
            mins = set_time//60
            secs = set_time%60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            await msg.edit(content="Time remaining: " + str(timer))
            time.sleep(1)
            set_time -= 1

        else:
            await message.channel.send('You have paused the at ' + mins + ':' + secs)
            return mins, secs
            
        

@client.event
# checks messages if from the bot itself
async def on_message(message):
    param = Param()
    param.mins +=1
    
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
        await message.channel.send('-pause to pause your session')
        
    if message.content.startswith('-set'):
        # timer(set)
        # set = await(message.channel.send('Enter the time in Minutes you would like:'))
        set = int(message.content.split(' ')[1])
        await message.channel.send('Your time has been set to ' + str(set) + ' minutes. Happy Studying!')
        await timer(set, 0, message)

    if message.content.startswith('-pause'):
        await timer(set, message, True)
        
# running the bot with token
# print(os.environ.get('TOKEN'))
# client.run(os.environ.get('TOKEN'))

