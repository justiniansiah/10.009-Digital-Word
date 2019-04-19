from libdw import sm

class Fruit(object):
    def relativeMovement(self):
        return (self.relativeRotation, self.unitsForward)
        
class Apple(Fruit):
    relativeRotation = 0
    unitsForward = 1
    
class Pear(Fruit):
    relativeRotation = -90
    unitsForward = 0
    
class Plum(Fruit):
    relativeRotation = 90
    unitsForward = 0
    
# a = Apple()
# print a.relativeMovement() #(0, 1)
# p = Pear()
# print p.relativeMovement() #(-90, 0)

class Herbivore(sm.SM):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.startState = 0
    
    def getNextValues(self,state,inp):
        (rot,dis) = inp.relativeMovement()
        if rot==0:
            if (state == 0 or state == 360):
                state = 0
                self.x+=1
                return state+rot,(self.x,self.y)
            
            
            elif state == 90:
                self.y+=1
                return state+rot,(self.x,self.y)
                
                
            elif state == 180:
                self.x-=1
                return state+rot,(self.x,self.y)
    
                
            elif state == 270 or state == -90:
                state = 270
                self.y-=1
                return state+rot,(self.x,self.y)
        else:
            return state+rot,(self.x,self.y)
        
h = Herbivore()
fruits = [Apple(), Apple(), Pear(), Apple(), Pear(), Apple()]
print h.transduce(fruits)