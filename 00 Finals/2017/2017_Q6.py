from math import sqrt

class Parallelogram(object):
    def __init__(self,side1,side2,diagonal):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self._diagonal = float(diagonal)
    
    def __str__(self):
        return "%0.2f"%(self._diagonal)
        
    def getd(self):
        return self._diagonal
        
    def setd(self,val):
        if val < 0:
            val = 0
        self._diagonal = val
    
    diagonal = property(getd,setd)
    
    def __call__(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self._diagonal
        output = True
        if s1+s2 < s3:
            output = False
        if s1+s3 < s2:
            output = False
        if s2+s3 < s1:
            output = False
        return output
    
    def calc_area(self):
        m = self.side1
        n = self.side2
        d = self._diagonal
        s = (m+n+d)/2

        area = 2*sqrt(s*(s-m)*(s-n)*(s-d))
        return round(area,2)

class Rhombus(Parallelogram):
    def __call__(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self._diagonal
        output = True
        if s1+s2 < s3:
            output = False
        if s1+s3 < s2:
            output = False
        if s2+s3 < s1:
            output = False
        if s1 != s2:
            output = False
        return output

    
class Rectangle(Parallelogram):
    def __call__(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self._diagonal
        if s3**2 != ((s1**2) + (s2**2)):
            return False
        else:
            return True


class Square(Rectangle):
    def __call__(self):
        s1 = self.side1
        s2 = self.side2
        s3 = self._diagonal
        if int((s3**2)) != ((s1**2) + (s2**2)):
            return False
        elif s1 != s2:
            return False
        else:
            return True    
    
    
    
    
    
    
    
# print "Test case 1"
# para = Parallelogram(2,3,4)
# print para #4.00
# 
# print "Test case 2"
# para = Parallelogram(2,3,4)
# para.diagonal = 3
# print para #3.00
# 
# 
# print "Test case 3"
# para = Parallelogram(2,3,4)
# para.diagonal = -1
# print para #0.00
# # 
# print "Test case 4"
# para = Parallelogram(3,4,5)
# print para() #True
# 
# print "Test case 5"
# para = Parallelogram(3,4,8)
# print para() #False

# print "Test case 6"
# rect = Rectangle(3,4,6)
# print rect() #False
# 
# print "Test case 7"
# rhom = Rhombus(3,3,2)
# print rhom() #True

# print "Test case 8"
# from math import sqrt
# squr = Square(2,2,3)
# print squr() #False
# squr = Square(2,2,sqrt(8))
# print squr() #True
# # 
# print "Test case 9"
# para = Parallelogram(3,4,2)
# print para.calc_area() #5.81
# 
# print "Test case 10"
# para = Parallelogram(5,7,9)
# print para.calc_area() #34.82
# 
# print "Test case 11"
# rect = Rectangle(3,4,5)
# print rect.calc_area() #12.0
# 
# print "Test case 12"
# rhom = Rhombus(3,3,4)
# print rhom.calc_area() #8.94
# 
# print "Test case 13"
# squr = Square(2,2,2.83)
# print squr.calc_area() #4.0
