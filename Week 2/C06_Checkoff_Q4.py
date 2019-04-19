from CheckoffQ4 import area_of_triangle

x1=raw_input("X coordinates of P1: ")
y1=raw_input("Y coordinates of P1: ")
x2=raw_input("X coordinates of P2: ")
y2=raw_input("Y coordinates of P2: ")
x3=raw_input("X coordinates of P3: ")
y3=raw_input("Y coordinates of P3: ")

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
x3=float(x3)
y3=float(y3)

class Coordinate:
    x = 0
    y = 0
    
p1= Coordinate ()
p1.x =x1
p1.y =y1
p2= Coordinate ()
p2.x =x2
p2.y =y2
p3= Coordinate ()
p3.x =x3
p3.y =y3


area = area_of_triangle (p1,p2,p3)

print "Area of triangle is %.2f square units." %(area)