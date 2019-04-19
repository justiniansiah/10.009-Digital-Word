import math
class Coordinate:
    x=0
    y=0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def get_maxmin_mag(f):
    pmin = -0.0
    pmax = -0.0
    for i in f:
        line = i.strip()
        LINE = line.split()
        
        x = float(LINE[0])
        y = float(LINE[1])
        
        pnew = math.sqrt(x**2 + y**2)
        
        if pnew > pmax:
            pmax = pnew
            Xmax = x
            Ymax = y
        elif pnew <= pmin:
            pmin = pnew
            Xmin = x
            Ymin = y
     
        
    pmax = Coordinate(Xmax,Ymax)
    pmin = Coordinate(Xmin,Ymin) 
        
    return pmax,pmin


f= open ("xy.dat","r")
pmax , pmin = get_maxmin_mag (f)
print "max: (%f, %f)"%( pmax.x, pmax.y) #( -1.000000 , -0.000000)
print "min: (%f, %f)"%( pmin.x, pmin.y) #(0.000000 , 0.000000)
