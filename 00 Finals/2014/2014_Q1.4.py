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
        
        
''' 1.4 : Define a new class ClosedPolyline2D that has the same functionality as Polyline2D. Closed
polylines form a closed loop in 2D. ClosedPolyline2D can have the same representation as
Polyline2D, with segments added to it in exactly the same way. The difference is that, implic-
itly, the very last vertex is connected to the starting vertex, thus that last segment need not be
added to the segment list explicitly.
The ClosedPolyline2D class must support all of the methods of the Polyline2D class addSegment, vertex, length. This new class must make use of Polyline2D and should
contain as little new code as possible.'''

class ClosedPolyline2D(Polyline2D):
    def length(self):
        total_length = Polyline2D.length(self)
        end_point  = self.startPoint
        n = len(self.segments)
        start_point = self.vertex(n)
        last_dx = end_point.x - start_point.x
        last_dy = end_point.y - start_point.y
        last_vec = Vector2D(last_dx, last_dy)
        total_length += last_vec.length()
        return total_length
        

cpline = ClosedPolyline2D(Point2D(1,2), [Vector2D(3,1)])
cpline.addSegment(Vector2D(1,0))
cpline.addSegment(Vector2D(0,2))
print cpline.length() #11.1622776602


        
