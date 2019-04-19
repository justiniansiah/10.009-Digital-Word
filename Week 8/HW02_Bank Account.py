class Account(object):
    def __init__(self,owner,account_number,amount):
        self.owner=owner
        self.account_number=account_number
        self.amount=amount
    
    def __str__(self):
        string ="%s, %s, balance: %s" %(self.owner,self.account_number,self.amount)
        return string
    
    def deposit(self,amount):
        self.amount += amount
        
    def withdraw(self,amount):
        self.amount -= amount
