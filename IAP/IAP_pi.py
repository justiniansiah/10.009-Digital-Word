import math
from math import pi

def fish(k):
    xx = 0
    for i in range (0,k):
        B = ((math.factorial(4*i)))*((1103+(26390*i)))
        C = ((math.factorial(i))**4)*(396**(4*i))
        D = B/C
        xx += D
    return xx
    
def estimate_pi():
    k=1
    pie = (A*fish(k))
    cake = 1/pie
    
    while (abs(cake - pi)> 1e-15):
        k+=1
        pie = A*fish(k)
        cake = 1/pie
        print (cake)
    return cake
        
        
A = (2*(math.sqrt(2)))/9801
ans = estimate_pi()
print(ans)