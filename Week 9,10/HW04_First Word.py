##Write a state machine whose inputs are the characters of a string and which outputs either (a) the input character if it is part of the first word on a line or (b) None. For the purposes here, a word is any sequence of consecutive characters that does not contain spaces or end-of-line characters. In this problem, comments have no special status, if the first thing on a line is '# ', then the first word is '#'.

#For example:

#>> str = 'def f(x): # comment\n   return 1'
# >>> m = FirstWordSM()
# >>> m.transduce(str)
# ['d', 'e', 'f', 
# None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, None, None, 
# 'r', 'e', 't', 'u', 'r', 'n', 
# None, None]
# >>> 
# Note: The end of line character is '\n', so you can test for an end of line with:
# 
#  
# if inp == '\n': 
# We encourage you to debug this on your machine in Idle or Canopy.
## 
from libdw import sm


class FirstWordSM(sm.SM):
    #startState = ''  # fix this
    startState = 0
    
    def getNextValues(self, state, inp):

        if state == 0:
            if inp == '#':      #start of comment
                next_state = 1
            elif inp == ' ' :   #end of word
                next_state = 3
                inp = None
            elif inp == '\n':   #end of word
                next_state = 0  #But i dont want this '\n'
                inp = None
            else:               #take the whole word
                next_state = 0
            
        elif state == 1:        #in comment
            if inp == '\n':
                next_state = 2  #comment has ended -> go to get new word
                inp = None
            else:               #still in comment
                next_state = 1
                inp = None
                
        elif state == 2:       #after end of comment
            if inp == ' ' or inp == "\n":     #still waiting for word after comment
                next_state = 2
                inp = None
            else:               
                next_state = 0
                        
        else:                   #state = 3: other words
            if inp == '#':      #start of comment
                next_state = 1
                inp = None
            elif inp == '\n':
                next_state = 2
                inp = None
            else:
                next_state = 3
                inp = None
        return next_state,inp
        
    def transduce(self,str):
        out = []
        self.start()
        for i in str:
            value = self.step(i) #step calls getNextsValues and returns output
            if value == '\n':
                pass                
            else:
                out.append(value)
        
        return out
        
str = 'def f(x): # comment\n   return 1'

m = FirstWordSM()
print m.transduce(str)
