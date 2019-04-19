
class Line0(object):
    def __init__(self,p1,p2):
        p1 = (float(p1[0]),float(p1[1]))
        p2 = (float(p2[0]),float(p2[1]))
        self.p1 = p1
        self.p2 = p2
        self.gradC()
    
    def gradC(self):
        self.grad = (self.p2[1]-self.p1[1])/(self.p2[0]-self.p1[0])
        self.C = self.p1[1]-self.grad*self.p1[0]
    
    def __call__(self,x):
        return (self.grad*x)+self.C

print "Test Case 0"
line = Line0((0,-1),(2,4))
print line(0.5),line(0),line(1) #0.25 -1.0 1.5

print "\n","Test Case 1"
line = Line0((0,-1),(2,4))
print line(0.5)                #0.25

print "\n","Test Case 2"
line = Line0((0,-1),(2,4))
print line(0)                  #-1.0

print "\n","Test Case 3"
line = Line0((0,-1),(2,4))
print line(1)                  #1.5

print "\n","Test Case 4"
line = Line0((3,3),(8,8))
print line(-1)                  #-1.0

print "\n","Test Case 5"
line = Line0((3,3),(8,8))
print line(4.3)                  #4.3