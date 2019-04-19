from libdw import sm

con = ['k','g','s','t','d','n','h','b','m','r']
vow = ['a','e','i','o','u']

class SpellCheckSM(sm.SM):
    startState = 'new word'
    def getNextValues(self,state,inp):
        if state == 'new word':
            if inp in con: #A1
                nextState = 'consonant'
                output = " "
            elif inp == ' ': #E10
                nextState = 'new word'
                output =' '
            else: #E8
                nextState = 'error'
                output = ' '
                
        elif state == 'consonant':
            if inp in vow: #A2
                nextState = 'vowel'
                output = ' '
            elif inp == ' ': #E4
                nextState = 'new word'
                output ='error'
            else: #E5
                nextState = 'error'
                output = ' '
        
        elif state == 'vowel':
            if inp == ' ': #A3
                nextState = 'new word'
                output = 'ok'
            
            else: #E6
                nextState = 'error'
                output = ' '
        
        else: #state = error
            if inp == ' ': #E7
                nextState = 'new word'
                output = 'error'
            else: #E9
                nextState = 'error'
                output = ' '
        return nextState,output
    
    
    
    
print 'Test case A'
a = SpellCheckSM()
line = 'a si tu ne mai me pas je '
print a.transduce(line)
print '\n'

print 'Test case B'
a = SpellCheckSM()
line = 'hi ka ru no de '
print a.transduce(line)
print '\n'
        
print 'Test case C'
a = SpellCheckSM()
line = 'mu '
a.transduce(line,verbose=True)
