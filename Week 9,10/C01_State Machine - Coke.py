from libdw import sm
class CM(sm.SM):
    # def __init__(self,startState=0):  # Not needed --> inherited from parent
    #     self.startState = startState
    
    startState = 0 #setting default startState
        
    def getNextValues(self,state,inp): 
    #takes in the current state and the input, and returns the next state and output as a tuple
    #This is defined in the parent class, but we are changing the method for this child class

        if state == 0:
            if inp == 100:
                next_state = 0
                output = (0,'coke',0)
            elif inp == 50:
                next_state = 1
                output = (50, '--',0)
            else:
                next_state = 0
                output = (0,'--',inp)
        
        elif state == 1:
            if inp == 100:
                next_state = 0
                output = (0,'coke',50)
            elif inp == 50:
                next_state = 0
                output = (0,'coke',0)
            else:
                next_state = 1
                output = (50,'--',inp)
        return next_state, output

c = CM()
c.start()
print c.step(100)
print c.step(50)
print c.state
    


