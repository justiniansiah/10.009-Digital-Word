######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

import math
def approx_ode2(h,t0,y0,tn):  #Runge-Kutta
    y = y0
    t = t0
    reps = int(tn/h)
    
    for i in range (reps):
        #Y = y(t) + h*((0.5*f(t,y(t)))+(0.5*f((t+h),y(t))+(h*f(t,y(t))))
        y = y + h*((0.5*f(t,y)) + (0.5*f((t+h),y)) + (h*f(t,y)))
        t += h
    return round(y,3)


def approx_ode(h,t0,y0,tn): #EUler's
    y = y0
    t = t0
    reps = int(tn/h)
    
    for i in range (reps):
        y += h*f(t,y)
        t+= h
       
    return round(y,3)    
    
def f(t, y):
    return 4.0 - t + (2.0*y)

    
#print approx_ode2(0.5,0,1,3)
#print approx_ode2(0.5,0,1,4)
print approx_ode(0.5,0,1,5)
print approx_ode2(0.5,0,1,5)