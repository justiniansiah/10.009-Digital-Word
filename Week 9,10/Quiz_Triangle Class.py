class Triangle(object):
    def __init__(self,color='green',filled = True,side1 = 1.0 ,side2 = 1.0,side3 = 1.0):
        self.color = color
        self.filled = filled
        self.side1= side1
        self.side2= side2
        self.side3= side3
    def perimeter(self):
        return self.side1+self.side2+self.side3

# t = Triangle()
# print t.color #green
# t= Triangle('blue')
# print t.color #blue
# t= Triangle()
# ans = (t.color,t.side1,t.side2,t.side3)
# print ans
# t= Triangle('red',False,4.0,3.0,5.0)
# ans = (t.color,t.filled,t.side1,t.side2,t.side3)
# print ans
t=Triangle(side1=4.0,side2=3.0,side3=5.0)
ans = t.perimeter()
print ans
    