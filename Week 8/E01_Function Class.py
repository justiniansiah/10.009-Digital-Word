import math

class F(object):
    def __init__(self,a,w):
        self.a = a
        self.w = w
        self.fn = FN
        
    def __call__(self,x):
        return self.fn(self.a,self.w,x)
        
def FN(a,w,x):
    A = math.exp(-a*x)
    B = math.sin(w*x)
    return A*B
        
        
f = F(a=1.0, w=0.1)
print f(x=math.pi)