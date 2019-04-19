from libdw import sm

class RingCounter(sm.SM):
    startState = 0
    def getNextValues(self,state,inp):
        if inp == 0:
            state +=1
            if state >7:
                return 0,'000'
            if state == 1:
                output = '001'
            elif state == 2:
                output = '010'
            elif state == 3:
                output = '011'
            elif state == 4:
                output = '100'
            elif state == 5:
                output = '101'
            elif state == 6:
                output = '110'
            else:
                state = 7
                output = '111'
                
        elif inp == 1:
            state = 0
            output = '000'
        return state,output
    
    
    
r = RingCounter()
print r.transduce([0,0,0,0,0,0,0,0,0])
print r.transduce([0,0,0,1,0,0,0,0,0])
print r.transduce([0,0,0,1,0,0,1,0,0])