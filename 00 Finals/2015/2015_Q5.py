class Square(object):
    def __init__(self,x=0,y=0,sideLength=1.0):
        self.x = x
        self.y = y
        self.sideLength = sideLength
    
    def getCenter(self):
        return (self.x,self.y)
    
    def getSideLength(self):
        return self.sideLength
    
    def getArea(self):
        return self.sideLength**2
        
    def getPerimeter(self):
        return self.sideLength*4
         
    def containPoint(self,px,py):
        if abs(px-self.x) <= self.sideLength/2 or self.x == px:
            if abs(py-self.y) <= self.sideLength/2 or self.y == py:
                return True
            else:
                return False
        else:
            return False
        
    def containSquare(self,insquare):
        (x,y) = insquare.getCenter()
        inlen2 = (insquare.getSideLength())/2.0
        if self.containPoint(x,y) and self.containPoint(x+inlen2,y) and self.containPoint(x-inlen2,y) and self.containPoint(x,y+inlen2) and self.containPoint(x,y-inlen2):
            return True
            
        else:
            return False

        
        
        
s = Square(x=1,y=1, sideLength=2.0)
# print s.getCenter() #(1,1)
# print s.getSideLength() #2.0
# print s.getArea() #4.0
#print s.getPerimeter() #8.0
# print s.containPoint(0,0) #True
# print s.containPoint(0,-0.5) #false
# print s.containPoint(1,1.5) #True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1))#True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1)) #False
        