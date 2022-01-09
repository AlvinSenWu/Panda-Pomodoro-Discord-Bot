class Clock:
    def __init__(self):
        self.mins = 0
        self.secs = 0

    def setMin(self, min):
        self.mins = min

    def getMin(self):
        return self.mins
    
    def setSec(self, sec):
        self.secs = sec

    def getSec(self):
        return self.secs

    def desc(self, total_sec):
        self.mins = total_sec // 60
        self.secs = total_sec % 60
        return '{:02d}:{:02d}'.format(self.mins, self.secs)

