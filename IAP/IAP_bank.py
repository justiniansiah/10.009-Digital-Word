class BankAccount:
    def __init__ (self,amt):
        self.acc = amt
    def withdraw(self,amt):
        if amt > self.acc:
            print("Insufficient funds")
        else:    
            self.acc -= amt
    
    def deposit (self,amt):
        self.acc += amt
        


class MinimumBalanceAccount (BankAccount):
    def __init__ (self,amt):
        self.acc = amt
    def withdraw(self,amt):
        if self.acc-amt < 1000:
            print("Insufficient funds")
        else:    
            self.acc -= amt

Myacc = MinimumBalanceAccount(100)

Myacc.deposit (1000)
#Myacc.withdraw (1000)

print ("Remaining Funds:$",Myacc.acc)