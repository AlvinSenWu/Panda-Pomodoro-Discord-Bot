import discord
import time

pau = False
class Clock:
    def __init__(self):
        self.mins = 0
        self.secs = 0
        self.pause = False
        self.stop = False

    def setMin(self, min):
        self.mins = min

    def getMin(self):
        return self.mins
    
    def setSec(self, sec):
        self.secs = sec

    def getSec(self):
        return self.secs

    async def setPause(self, pau):
        print("executed")
        self.pause = pau 
        print("pause", self.pause)
    
    def getPause(self):
        return self.pause

    def setStop(self, sto):
        self.stop = sto
    
    def getStop(self):
        return self.stop

    async def starttimer(self, message):
        # set_time = set_time*60
        # 
        # mins = 0
        # secs = 0
        set_time = self.mins*60 + self.secs
        msg = await message.channel.send('{:02d}:00'.format(self.mins))
        mins = 0
        secs = 0
        while set_time:
            # mins, secs = divmod(set_time, 60)
            print(pau)
            if not pau:
                # mins = set_time//60
                # secs = set_time%60
                self.mins = set_time//60
                self.secs = set_time%60
                timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
                print(timer, end="\r")
                await msg.edit(content="Time remaining: " + str(timer))
                time.sleep(1)
                set_time -= 1
            elif pau:
                await message.channel.send('Your session has paused at {:02d}:{:02d}'.format(self.mins, self.secs))
                await message.channel.send('To resume type -r')
                return
            elif self.stop:
                await message.channel.send('Your session has stopped')
                await message.channel.send('To Start another set, type -set[enter time in minutes]')
                self.mins = 0
                self.secs = 0
                self.pause = 0
                self.stop = 0
                return


        if not set_time:
            await msg.edit(content="Time remaining: 00:00")
            await message.channel.send('Your session has ended. Great Work!')
            await message.channel.send('To Start another set, type -set[enter time in minutes]')
            await message.channel.send('For list of commands type -c')