import math
def simpsons_rule(fn,n,a,b):
    b = float(b)
    a = float(a)
    h = (b-a)/n
    B = 0.0
    C = 0.0
    x = a
    
    for i in range (1,((n/2))):
        x = 2*i
        y = a+(x*h)
        B += 2*fn(y)
        
    for i in range (1,(n/2+1)):
        x = (2*i)-1
        y = a+(x*h)
        C += 4*fn(y)
        
    ans = (h/3)*(B+C+fn(a)+fn(b))
    ans = round(ans,2)
    return ans

def fn(x):
    return x**2 #x^2
    #return math.sin(x) #sin(x)
    #return (math.e)**(-x) #e^-x
    
print simpsons_rule(fn,1000,1,3) #x^2
#print simpsons_rule(fn,1000,0,math.pi) #sin(x)
#print simpsons_rule(fn,1000,-1,1) #e^-x

    