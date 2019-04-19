
class MyTask(object):
    def __init__(self, deadline, duration):
        self.deadline = deadline
        self.duration = duration
        
    def __str__(self):
        return 'T(%d,%d)' %(self.deadline, self.duration)

def procrastination(assignments):
    totalTime=0
    firstDead=assignments[0].deadline
    lastDead=assignments[0].deadline
    for i in assignments: 
        totalTime += i.duration      #Find out total time needed
        if i.deadline < firstDead: #Find out when first deadline
            firstDead = i.deadline
        if i.deadline > firstDead: #Find out when last deadline
            firstDead = i.deadline
    
    if lastDead-totalTime <0:

        return -1 #Total Time required exceeds time needed even if start at 0
    else:
        no = 0 #number of assignments due at 1st deadline
        firstDur = 0
        for i in assignments: 
            if i.deadline == firstDead:
                no += 1
                firstDur += i.duration
        
        time = firstDead - firstDur
        dur = 0
        for i in assignments:
            dur += i.duration
            if time + dur > i.deadline:
                time-=1

                
            
        return time
        
    







# 
# assignments = [ MyTask(9,1), MyTask(9,2), MyTask(7,1) ]
# print procrastination(assignments)
# 
# assignments1 = [ MyTask(3,2), MyTask(3,2) ]
# print procrastination(assignments1)

assignments2 = [ MyTask(9,1), MyTask(9,2), MyTask(4,3) ]
print procrastination(assignments2)
# 
# assignments3 = [MyTask(14,10), MyTask(33,2), MyTask(5,3), MyTask(14,1), MyTask(10,2)]
# print procrastination(assignments3)