import math
def approx_ode(h,t0,y0,tn):
    y = y0
    t = t0
    reps = int(tn/h)
    
    for i in range (reps):
        y += h*f(t,y)
        t+= h
        
        
        
    return round(y,3)    
    
def f(t, y):
    return 3.0+math.exp(-t)-0.5*y
    
print approx_ode(0.1,0,1,3)
print approx_ode(0.1,0,1,4)
print approx_ode(0.1,0,1,5)
