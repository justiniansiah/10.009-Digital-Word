from math import pi as pi
from math import sqrt as sqrt

# class square(object):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# 
# def countLitPixel(cx,cy,r):
#     areaC = pi*r**2
#     areaS = r**2
#     count = 0
#     startx = cx-r
#     starty = cy-r
#     lengthc = sqrt(cx**2+cy**2)
#     for i in range(2*r):
#         for j in range(2*r):
#             curx = startx+i
#             cury = starty+j
#             length = sqrt(cx**2+cy**2) 
#             if length <= lengthc:
#                 count+=1

def countLitPixel(cx,cy,r):
    count = 0
    for i in range(r):
        for j in range(0,r):
            y = sqrt(r**2-i**2)            
            if j < y:
                count +=1

    return count*4
    
print countLitPixel(5,2,5) #88
print countLitPixel(1,1,1) #4