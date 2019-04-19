from libdw import sm

class SimpleAccount(sm.SM):

# # #   
#     def __init__(self,startBalance):
#         self.Balance = startBalance
#         if startBalance < 100:
#             self.startState = 1
#         else:
#             self.startState = 0
#         
#     def getNextValues(self,state,inp): 
#         if state == 0:
#             self.Balance += inp
#             if self.Balance <100:
#                 next_state = 1
#             else:
#                 next_state = 0
#             
#         elif state == 1:
#             self.Balance += inp
#             if self.Balance <100 and inp < 0:
#                 self.Balance -= 5
#                 next_state = 1
#             else:
#                 next_state = 0
#             
#         return next_state,self.Balance
# # #    
    startState = 0
    
    def __init__(self, start_balance):
        self.startState = start_balance
        
    def getNextValues(self,state,inp):
        if state < 100 and inp < 0: #withdrawal when less than 100
            next_state = state + inp - 5
        else:
            next_state = state + inp
        output = next_state
        return next_state,output


acct = SimpleAccount(110)
acct.start()
print acct.step(10)
print acct.step(-25)
print acct.step(-10)
print acct.step(-5)
print acct.step(20)
print acct.step(20)
