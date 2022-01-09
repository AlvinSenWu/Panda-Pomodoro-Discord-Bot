import discord
import time
import os
from clock import Clock

client = discord.Client()


@client.event
async def on_ready():
    print('{0.user} is now running!'.format(client))

# async def timer(param, message, pause=False, stop=False):
#     # set_time = set_time*60
#     # 
#     # mins = 0
#     # secs = 0
#     set_time = param.getMin()*60 + param.getSec()
#     msg = await message.channel.send('{:02d}:00'.format(param.getMin()))
#     mins = 0
#     secs = 0
#     while set_time:
#         # mins, secs = divmod(set_time, 60)
#         print(param.getPause())
#         if not param.getPause():
#             # mins = set_time//60
#             # secs = set_time%60
#             param.setMin(set_time//60)
#             param.setSec(set_time%60)
#             timer = '{:02d}:{:02d}'.format(param.getMin(), param.getSec())
#             print(timer, end="\r")
#             await msg.edit(content="Time remaining: " + str(timer))
#             time.sleep(1)
#             set_time -= 1
#         elif param.getPause():
#             await message.channel.send('Your session has paused at {:02d}:{:02d}'.format(mins, secs))
#             await message.channel.send('To resume type -r')
#             return
#         elif param.getStop():
#             await message.channel.send('Your session has stopped')
#             await message.channel.send('To Start another set, type -set[enter time in minutes]')
#             param.setMin(0)
#             param.setSec(0)
#             param.setPause(False)
#             param.setStop(False)
#             return


#     if not set_time:
#         await msg.edit(content="Time remaining: 00:00")
#         await message.channel.send('Your session has ended. Great Work!')
#         await message.channel.send('To Start another set, type -set[enter time in minutes]')
#         await message.channel.send('For list of commands type -c')
            

@client.event
# checks messages if from the bot itself
async def on_message(message):
    clock = Clock()

    pause = False
    
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
        # clock.setMin(int(message.content.split(' ')[1]))
        await message.channel.send('Your time has been set to ' + str(clock.getMin()) + ' minutes. Happy Studying!')
        # await clock.starttimer(message)

        getMin = int(message.content.split(' ')[1])
        getSec = 0
        
        set_time = getMin*60 + getSec

        msg = await message.channel.send('{:02d}:00'.format(getMin))
        mins = 0
        secs = 0
        while set_time:
            # mins, secs = divmod(set_time, 60)
            # print(param.getPause())
            print(pause)
            if not pause:
                # mins = set_time//60
                # secs = set_time%60
                getMin = set_time//60
                getSec = set_time%60
                timer = '{:02d}:{:02d}'.format(getMin, getSec)
                print(timer, end="\r")
                await msg.edit(content="Time remaining: " + str(timer))
                time.sleep(1)
                set_time -= 1
            elif pause:
                print('should be paused')
                await message.channel.send('Your session has paused at {:02d}:{:02d}'.format(mins, secs))
                await message.channel.send('To resume type -r')
                return pause 


        if not set_time:
            await msg.edit(content="Time remaining: 00:00")
            await message.channel.send('Your session has ended. Great Work!')
            await message.channel.send('To Start another set, type -set[enter time in minutes]')
            await message.channel.send('For list of commands type -c')

    if message.content.startswith('-pause'):
        pause = True
        print(pause)
        return pause

    if message.content.startswith('-r'):
        clock.setPause(False)

    if message.content.startswith('-stop'):
        clock.setStop(True)
        
# running the bot with token
# print(os.environ.get('TOKEN'))
client.run('OTI4NzA2NTYzNzAxNjM3MTgw.YdcrYw.mLqzxQt-uTTpnDwwkdE7eysH2aA')