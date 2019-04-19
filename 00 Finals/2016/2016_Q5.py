

class Avatar(object):
    def __init__(self,name,hp=100,position = (1,1)):
        self.name = name
        self.hp = hp
        self.position = position
        
    
    def getName(self):
        return self.name
        
    def setName(self,name):
        self.name = name
        
    def getHP(self):
        return self.hp
        
    def setHP(self,hp):
        self.hp = hp
        
    def getPosition(self):
        return self.position
        
    def setPosition(self,position):
        self.position = position
        
    changeName = property(getName,setName)
    changeHP = property(getHP,setHP)
    changePosition = property(getPosition,setPosition)
    
    def heal(self,heal=1):
        if heal <0:
            pass
        else:
            #changeHP(heal)
            self.setHP(self.hp+heal)
    
    def attacked(self,dmg=-1):
        if dmg >0:
            pass
        else:
            #changeHP(dmg)
            self.setHP(self.hp+dmg)
            
# a = Avatar('John')
# print (a.name,a.hp,a.position)

# a = Avatar('Jane',150,(10,10))
# print (a.name,a.hp,a.position)
    
a = Avatar('John')
# a.setName('Jude')
# print a.getName()

# a.setPosition((1,3))
# print a.getPosition()

a.setHP(200)
a.heal(5)
a.attacked()
print a.getHP()
    
    
    