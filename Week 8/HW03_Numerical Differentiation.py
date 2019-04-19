from math import *
import math
#return only the derivative value without rounding
#your return value is a float, which is the approximate value of the derivative
#Tutor will compute the approximate error based on your return value

class Diff(object):
    def __init__(self,f,h=1E-4):
        self.f = f
        self.h = h
    
    def __call__(self,x):
        return ((self.f(x+self.h))-self.f(x))/(self.h)
        
# 
# def f(x):
#     return 0.25*x**4
# 
# df = Diff(f)
# 
# for x in (1, 5, 10):
#     df_value = df(x) # approx value of derivative of f at point x
#     exact = x**3 # exact value of derivative
#     print "f'(%d)=%g (error = %.2E)" %(x, df_value , exact - df_value )

df = Diff(math.log,0.1)
print df(10.0)