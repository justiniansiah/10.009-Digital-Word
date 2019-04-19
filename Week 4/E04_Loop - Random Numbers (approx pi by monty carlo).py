import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

# def Sq(n):
#     return 4*(n**2)
# def Circ(n):
#     return math.pi*(n**2)

def pi_approx_by_monte_carlo(n):
    S = 0.0
    x = y = 0.0
    C = 0
    for i in range(n):
        S+=1
        x = random.random()
        y = random.random()
        rcheck = (x**2) + (y**2)
        if rcheck <= 1:
            C+=1

    return round(4*C/(n+1.0),2)
        
        
print pi_approx_by_monte_carlo(100) #3.2
print pi_approx_by_monte_carlo(10000) #3.15
print pi_approx_by_monte_carlo(100000) #3.15
#print pi_approx_by_monte_carlo(10000000) #3.14
        
        
        