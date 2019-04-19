class Matrix:
    s = "Matrix A"
    f = "%6.2f"    
    def __init__(self,m,s,f):
        self.m = m
        self.s = s
        self.f = f
        
    def __str__(self):
        n = len(self.m)
        line1 = "%s: Rows: %d Columns: %d"%(self.s,n,n)
        string =line1+"\n"
        for i in range(n):
            string2 =""
            for j in range(n):
                string2+= self.f%self.m[i][j]
            string +=  string2 + "\n"
        
        return string
        
    def diag(self):
        ret = True
        for i in range(len(self.m)):
            if self.m[i][i] == 0:
                ret = False
        return ret
        
    def upperDiag(self):
        ret = True
        for i in range(len(self.m)-1):
            if self.m[i][i+1] == 0:
                ret = False
        return ret
        
        
    def lowerDiag(self):
        ret = True
        for i in range(len(self.m)-1):
            if self.m[i+1][i] == 0:
                ret = False
        return ret
        
    def triDiag(self):
        ret = False
        a = self.diag()
        b = self.upperDiag()
        c = self.lowerDiag()
        if a == True and b == True and c == True:
            ret = True
        return ret
        
m1 =[[1 ,4 ,0 ,0] , [3, 4, 1, 0], [0, 2, 3, 4], [0 ,0 ,1 ,3]]
m2 =[[1 ,0 ,0 ,0] , [3, 4, 1, 0], [0, 2, 3, 4], [0 ,0 ,1 ,3]]
m3 =[[1 ,4 ,0 ,0] , [3, 0, 1, 0], [0, 2, 3, 4], [0 ,0 ,1 ,3]]

s = "Matrix A"
f = "%6.2f"
a= Matrix (m1,s,f)
b =Matrix (m2,s,f)
c= Matrix (m3 , "DW Matrix ", " %6.1f")
print c
