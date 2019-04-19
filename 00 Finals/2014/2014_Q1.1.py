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
        newx
        
        
class Vector2D:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    def length(self):
        return math.sqrt(self.dx**2 + self.dy**2)
        
'''1.1: Write a method add in the Point2D class that adds a Vector2D to a Point2D, resulting in
another Point2D. Make sure that your method does not change the values of the arguments.'''


p = Point2D(1,2)
v = Vector2D(3,1)
q = p.add(v)
print q #Point2D(4,3)