def times(x,y,z):
    b = x
    if y>1:
        b = b*z
        y-=1
        times (b,y,z)
    else:
        print b
        
def power (x,y):
    times (x,y,x)
    
    
power (3,3)
    
        
    
    