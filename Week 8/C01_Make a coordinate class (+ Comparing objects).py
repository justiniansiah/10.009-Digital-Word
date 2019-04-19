from math import sqrt as sqrt

class Coordinate:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def magnitude(self):
        return sqrt(self.x**2+self.y**2)
    
    def translate(self, dx, dy):
        self.x+=dx
        self.y+=dy
        return        
        
    def __eq__(self, other):            #IMPORTANT: If you want to compare object values
        if self.x == other.x and self.y==other.y:
            out = True
        else:
            out = False
        return out
    
p = Coordinate()
print p.x, p.y
print p.magnitude()

p.x = 3
p.y = 4
print p.magnitude()

q = Coordinate(3,4)
print p == q        #comparing object values

q.translate(1,2)
print q.x

print p == q