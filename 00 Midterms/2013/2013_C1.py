import math
def roots(a,b,c):
    C = math.sqrt((b**2)-(4*a*c))
    ans1 = (-b+C)/(2*a)
    ans2 = (-b+C)/(2*a)
    return ans1,ans2
    
print roots(5,50,125)
