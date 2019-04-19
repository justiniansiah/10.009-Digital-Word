class Animal:
    def __init__(self,List):
        self.name = List[0]
        self.weight = List[1]
        self.type = List[2]
        
    def setAttrib(self,k,v):
        if k == 0:
            self.name = v
        elif k == 1:
            self.weight = v
        elif k == 2:
            self.type = v
        
    def __call__(self):
        List = [self.name,self.weight,self.type]
        return List
    
    def __str__(self):
        return "Name: {0} Weight: {1}Kg Type: {2}".format(self.name, self.weight, self.type)
        
     

a= Animal (["Snoopy", 10, "Dog"])
a.setAttrib(1,12)
print a()
        