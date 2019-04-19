count = 1

class Visitor(object):
    def __init__(self,name = 'Visitor'):
        global count
        if name == 'Visitor':
            self.name = 'Visitor ' + str(count)
        else:
            self.name = name
        
        count +=1
        self.time = 1
          
    def setName(self,name):
        self.name = name
        
    def __call__(self):
        out = "%s called the %rth time" %(self.name,self.time)
        self.time +=1
        return out        

v1=Visitor('John')
print v1()
v2=Visitor()
print v2()
print v1()
v2.setName('Marina')
print v2()
        