##Write a state machine whose inputs are the characters of a string (representing a Python program) and which outputs either (a) the input character if it is part of a comment or (b) None. As you know, comments start with a '#' character and continue to the end of the current line.

#For example:

# >> str = 'def f(x): # comment\n   return 1'
# >>> m = CommentsSM()
# >>> m.transduce(str)
# [None, None, None, None, None, None, None, None, None, None, 
# '#', ' ', 'c', 'o', 'm', 'm', 'e', 'n', 't', 
# None, None, None, None, None, None, None, None, None, None, None, None]
# Note: The end of line character is '\n', so you can test for an end of line with:
# 
# if inp == '\n': 
# You should start by drawing a state transition diagram indicating the states and what inputs cause transition to which other states.
# 
# In Python, if you want to create a string that contains new line character, you can use '\n'.
from libdw import sm

class CommentsSM(sm.SM):
    #startState = ''  # fix this
    startState = 0
    
    def getNextValues(self, state, inp):

        if state == 0:
            if inp == '#':
                next_state = 1
            else:
                inp = None
                next_state = 0
            
        else: #state == 1
            if inp == '\n':
                inp = None
                next_state = 0
            else: #still in comment
                next_state = 1
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
#str = "#initial comment \n def f(x):  # func \n if x:   # test\n# comment\n return 'foo'"
m = CommentsSM()
print m.transduce(str)

