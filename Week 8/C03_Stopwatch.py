import time

class StopWatch(object):
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1
        
    def start(self):
        self.start_time = time.time()
        self.end_time = -1
        return
    
    def stop(self):
        self.end_time = time.time()
        return
        
    def elapsed_time(self):
        if self.end_time == -1:
            ans = None
        else:
            ans = self.end_time - self.start_time
            ans *= 1000
            ans = round(ans,1)
        return ans
        
sw = StopWatch()
time.sleep(0.1)
sw.stop()
print sw.elapsed_time()
sw. start ()
time.sleep (0.2)
print sw. elapsed_time ()
sw. stop ()
print sw. elapsed_time ()

# sw = StopWatch()
# sw.start()
# time.sleep(10)
# sw.stop()
# print sw.elapsed_time()