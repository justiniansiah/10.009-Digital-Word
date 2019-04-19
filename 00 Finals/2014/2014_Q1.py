import math

class Point2D(object): 
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return 'Point2D('+ str(self.x)+',' + str(self.y)+')'
    def add(self,v):
        return Point2D(self.x+v.dx,self.y+v.dy)
    

class Vector2D(object):
    def __init__(self,dx,dy):
        self.dx=dx
        self.dy=dy
    def length(self):
        return math.sqrt(self.dx**2 + self.dy**2)
        
# p = Point2D(1,2)
# v = Vector2D(3,1)
# q = p.add(v)
# print q #Point2D(4,3)

class Polyline2D(object):
    def __init__(self,start,vlist):
        self.start = start
        self.vlist = vlist
        
    def addSegment(self,seg):
        self.vlist.append(seg)
        
    def length(self):
        length = 0
        for vec in self.vlist:
            length += vec.length()
        return length
        
    def vertex(self,no):
        start = self.start
        for i in range(no):
            start = start.add(self.vlist[i])
        return start
    
# pline = Polyline2D(Point2D(1,2),[Vector2D(3,1)])
# pline.addSegment(Vector2D(1,0))
# pline.addSegment(Vector2D(0,2))
# #print pline.length() #6.16227
# print pline.vertex(0)
# print pline.vertex(1)
# print pline.vertex(2)
# print pline.vertex(3)

class  ClosedPolyline2D(Polyline2D):
    def length(self):
        length = 0
        for vec in self.vlist:
            length += vec.length()
        last = self.vertex(len(self.vlist))
        print self.start
    
        lastl = math.sqrt(((self.start.x-last.x)**2) + ((self.start.y-last.y)**2))
        return length + lastl
            
            
cpline = ClosedPolyline2D(Point2D(1,2),[Vector2D(3,1)])
cpline.addSegment(Vector2D(1,0))
cpline.addSegment(Vector2D(0,2))
print cpline.length() #11.162