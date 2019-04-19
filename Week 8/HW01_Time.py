class Time(object):
    def __init__(self,hours,minutes,seconds):
        self._hours=hours
        self._minutes=minutes
        self._seconds = seconds
    def __str__(self):
        return "Time: %d:%d:%d"%(self._hours,self._minutes,self._seconds)
    
    def get_time(self):
        return (self._hours*3600) + (self._minutes*60) + self._seconds
    
    def set_time(self,value):    
        hour= value/3600
        if hour > 23:
            hour %= 24
        self._hours = hour
        min = value%3600
        self._seconds = min%60
        self._minutes = min/60
        return
        
    elapsed_time = property(get_time,set_time)

t = Time(10,19,10)
print t.elapsed_time
#t.elapsed_time = 555550
#t.elapsed_time = 45550 #45550
t.elapsed_time = 508550 #Time: 21:15:50
print t.elapsed_time
print t