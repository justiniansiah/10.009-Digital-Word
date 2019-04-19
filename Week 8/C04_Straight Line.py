class Line():
    def __init__(self,c0,c1):
        self.c0 = c0
        self.c1 = c1
    
    def __call__(self,x):
        return round(self.c0+self.c1*x,2)
        
    def table(self,L,R,n):
        interval = (R-L)/float(n-1)
        string = ""
        if L == R:
            n=1
        for i in range(n):
            x = L + (i*interval)
            y = self(x)
            string += "%10.2f"%(x)
            string += "%10.2f"%(y)
            string += "\n"
        if n==0:
            string = "Error in printing table"
        return string
        
def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)

#print testLine(1,2,2,1,5,4)  #c0 = 1, c1 = 2, x = 2, L = 1, R = 5, N = 4
#print testLine(-1,2,2,-1,5,10) #c0 = -1, c1 = 2, x = 2,  L = -1, R = 5, N = 10
#print testLine(1,2,2,1,5,4)  #c0 = 1, c1 = 2, x = 2, L = 1, R = 5, N = 4
#print testLine(3,4,2,1,5,0)  #c0 = 1, c1 = 2, x = 2, L = 1, R = 5, N = 4
print testLine(3,4,2,1,1,15)  #c0 = 3, c1 = 4, x = 2, L = 1, R = 1, N = 15