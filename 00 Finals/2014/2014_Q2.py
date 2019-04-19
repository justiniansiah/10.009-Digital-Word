from libdw import sm

class CombLock(sm.SM):
    def __init__(self,keyList):
        self.list = keyList
        self.store = []
    
    def getNextValues(self,state,inp):
        if inp == 0 :
            state = 'locked'
            return state,state
            
        elif inp >=1 and inp <= 9:
            self.store.append(inp)
            state = 'locked'
            return state,state
            
        elif inp == -1:
            if len(self.list) == len(self.store):
                for i in range(len(self.list)):
                    if self.list[i] == self.store[i]:
                        pass
                    else: 
                        state = 'locked'
                        self.store = []
                        return state,state
                state = 'unlocked'
                self.store = []
                return state,state
    
            else: 
                state = 'locked'
                self.store = []
                return state,state
            
# lock = CombLock([1,2,5])
# print lock.transduce([1,2,5,-1])
# print lock.transduce([1,0,2,5,-1])
# print lock.transduce([3,2,5,-1])
# print lock.transduce([1,2,5,-1,1,2,5,-1])
# print lock.transduce([3,2,5,-1,1,2,5,-1])

def mapT2P(x,y):
    if 0 <= x and x <= 3:
        if 0 <= y and y <= 3:
            return 1
        if 4 <= y and y <= 7:
            return 4
        if 8 <= y and y <= 11:
            return 7
    if 4 <= x and x <= 7:
        if 0 <= y and y <= 3:
            return 2
        if 4 <= y and y <= 7:
            return 5
        if 8 <= y and y <= 11:
            return 8
    if 8 <= x and x <= 11:
        if 0 <= y and y <= 3:
            return 3
        if 4 <= y and y <= 7:
            return 6
        if 8 <= y and y <= 11:
            return 9

class TouchMap(sm.SM):
    startState = 0
    def getNextValues(self,state,inp):
        (e,x,y) = inp
        currentState = mapT2P(x,y)
        if e == 'TouchUp':
            return currentState,-1
        elif e == 'TouchDown':
            return currentState,mapT2P(x,y)
        else:
            if state == currentState:
                return currentState,0
            else:
                return currentState,currentState
            
        
        
        
m = TouchMap()
print m.transduce([('TouchDown',2,2), ('TouchUpdate',3,3), ('TouchUp',4,4)])    
print m.transduce([('TouchDown',3,3), ('TouchUpdate',4,3), ('TouchUp',4,4)]) 
        
        