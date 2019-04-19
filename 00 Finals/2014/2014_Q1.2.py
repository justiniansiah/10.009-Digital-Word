'''Develop a Python class to represent polylines. A polyline is a piecewise linear curve - one can
think of it as a series of connected line segments. The polyline class will build upon the two
classes below, which represents points and vectors.'''

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
        
'''1.2: Implement the Polyline2D class, which has the following two methods. (Write your code and
test it in IDLE, and submit your answers via Tutor.)
init : takes two arguments. The rst argument is an instance of Point2D representing the
start of the polyline. The second argument is a list of instances of Vector2D, which represents
the consecutive line segments of the polyline.
addSegment: adds a line segment to the end of the polyline. It takes one argument, which is
the new line segment represented as an instance of Vector2D. It does not need to return any
value.'''

class Polyline2D:
    def __init__(startP,segments):
        self.startPoint = startP
        self.segments = segments
        
    def addSegment(self,new_v):
        self.segments.append(new_v)
        