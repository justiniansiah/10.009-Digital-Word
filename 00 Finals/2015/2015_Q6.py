from libdw import sm

class Elevator(sm.SM):
    startState = 'First'
    
    def getNextValues(self,state,inp):
        
        if state == 'First':
            if inp == 'Up':
                next_state = 'Second'
            else:
                next_state = 'First'
        
        elif state == 'Second':
            if inp == 'Up':
                next_state = 'Third'
            else:
                next_state = 'First'
        
        else:
            if inp == 'Up':
                next_state = 'Third'
            else:
                next_state = 'Second'
        output = next_state
        return next_state,output

e = Elevator()
print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])