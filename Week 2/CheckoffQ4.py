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
