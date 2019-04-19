from math import sqrt

class Coordinate:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    side1 = sqrt(((p1.x-p2.x)**2)+((p1.y-p2.y)**2))
    side2 = sqrt(((p3.x-p2.x)**2)+((p3.y-p2.y)**2))
    side3 = sqrt(((p1.x-p3.x)**2)+((p1.y-p3.y)**2))
    s = (side1 + side2 + side3)/2
    
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area

print " Test Case 1"
p1= Coordinate ()
p1.x =1.5
p1.y= -3.4
p2= Coordinate ()
p2.x =4.6
p2.y=5
p3= Coordinate ()
p3.x =9.5
p3.y= -3.4
ans = area_of_triangle (p1,p2,p3)
print ans