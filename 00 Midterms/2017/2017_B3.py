#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

import math

def area_r_polygon(n, s):
    A = n*s**2
    B = 4*math.tan(math.pi/n)
    return round(A/B,3)
    
print area_r_polygon(5,6.5) #72.69
print area_r_polygon(7,3.25) #38.383
print area_r_polygon(2,12.5) #0.0
    
    


