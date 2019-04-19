'''Develop a Python class to represent polylines. A polyline is a piecewise linear curve - one can
think of it as a series of connected line segments. The polyline class will build upon the two
classes below, which represents points and vectors.'''

import math 

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point2D(' + str(self.x) + ',' + str(self.y) + ')'
    def add(self,val):
        return Point2D(self.x+val.dx,self.y+val.dy)
        
class Vector2D:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    def length(self):
        return math.sqrt(self.dx**2 + self.dy**2)

class Polyline2D:
    def __init__(self,startP,segments):
        self.startPoint = startP
        self.segments = segments
        
    def addSegment(self,new_v):
        self.segments.append(new_v)
        
    def length(self):
        total_length = 0.0
        for vec in self.segments:
            total_length += vec.length()
        return total_length
        
    def vertex(self,idx):
        cur_point = self.startPoint
        for i in range(idx):
            cur_vec = self.segments[i]
            cur_point = cur_point.add(cur_vec)
        return cur_point
            
        
'''1.3: Implement the following methods of the Polyline2D class.
length: returns the total length of the polyline, which is the sum of the lengths of the seg-
ments. This method has no arguments. You must use Vector2D 's length method in your
implementation.
vertex: takes an integer index and returns the polyline vertex, represented as an instance of
Point2D, at that index. The starting point of the polyline is vertex 0, and you can assume that
the index you are given is legal.'''

pline = Polyline2D(Point2D(1,2), [Vector2D(3,1)])
pline.addSegment(Vector2D(1,0))
pline.addSegment(Vector2D(0,2))
print pline.length() #6.16227766017
print pline.vertex(0) #Point2D(1,2)
print pline.vertex(1) #Point2D(4,3)
print pline.vertex(2) #Point2D(5,3)
print pline.vertex(3) #Point2D(5,5)
        