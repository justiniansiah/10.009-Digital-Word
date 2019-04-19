import math
def approx_pi(n):
    a = (2*math.sqrt(2))/9801.0
    d = 0
    for i in range (0,n):
        b = (math.factorial(4.0*i))*(1103.0+(26390*i))
        c = ((math.factorial(i))**4)*(396.0**(4*i))
        d = d+(b/c)
    return 1/(a*d)

print approx_pi(1)
