import math
def f(x):
    return math.exp(x)
def trapezoidal(a,b):
    return round((b-a)*(f(b)+f(a))/2,2)

print trapezoidal(6,5)
print trapezoidal(2,2)    
print trapezoidal(2,5)
print trapezoidal(3,2)
    