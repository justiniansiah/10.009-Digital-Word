from libdw import sm
class RunOfEvenNumbers(sm.SM):
   
    
    startState = 0 #setting default startState
    #0 odd
    #1 even
    def __init__(self):
        self.length = 0
            
    def getNextValues(self,state,inp): 
        if state == 0:
            if inp % 2 == 0:
                state = 1
                self.length +=1
            else:
                state = 0
                self.length = 0
        else:
            if inp % 2 == 0:
                state = 1
                self.length +=1
            else:
                state = 0
                self.length = 0
        return state,self.length
        
m = RunOfEvenNumbers()
print m.transduce([1,2,3,7,4,2,7,2,8,2,8])
print m.transduce([2,2,2,1,2,2,2,1,2,1,2,1,2,1])

    


