import copy

class Polynomial(object):
    def __init__(self,list):
        self.coeff = list
    
    #Addition of 2 polynomials    
    def __add__(self,other):
        sLength = min(len(self.coeff),len(other.coeff))
        if len(self.coeff) > len(other.coeff):
            list = copy.deepcopy(self.coeff)
            for i in range(sLength):
                list[i] += other.coeff[i]
                
        else:
            list = copy.deepcopy(other.coeff)
            for i in range(sLength):
                list[i] += self.coeff[i]
                
        return Polynomial(list)
    
    #Subtraction of 2 polynomials
    def __sub__ (self,other):
        sLength = min(len(self.coeff),len(other.coeff))
        if len(self.coeff) > len(other.coeff):
            list = copy.deepcopy(self.coeff)
            for i in range(sLength):
                list[i] -= other.coeff[i]
                
        else:
            list = copy.deepcopy(other.coeff)
            for i in range(len(list)):
                list[i] = -list[i] #make coefficients in list negative
                
            for i in range(sLength):
                list[i] += self.coeff[i] #add the coeff from 'self'
                
        return Polynomial(list)
     
    #returns the value given x
    def __call__(self,x):
        sum = 0
        for i in range(len(self.coeff)):
            sum += (self.coeff[i])*(x**i)
        return sum
        
    #Multiply 2 polynomials
    def __mul__(self,other):
        list = []
        for i in range (len(other.coeff) +len(self.coeff)-1): #making an empty list with size M + N
            list.append(0)
        for i in range(len(other.coeff)):
            for j in range(len(self.coeff)):
                list[i+j] += self.coeff[j]*other.coeff[i]
       
        # #removing extra 0's at the end
        # check = True
        # ck = 0
        # iList = list[::-1]
        # while check:
        #     if iList[ck] == 0:
        #         list.pop(len(list)-ck-1)
        #         ck += 1
        #     else:
        #         check = False

        return Polynomial(list)
        
    #Differentiate
    def differentiate(self):
        self.coeff.pop(0)
        for i in range(len(self.coeff)):
            self.coeff[i]*=(i+1)
        return None
    
    #Derivative
    def derivative(self):
        new = copy.deepcopy(self)
        new.differentiate()
        return new
        
    
#==============================================================================
#         
# p1 = Polynomial ([1 , -1])
p2 = Polynomial ([0 , 1, 0, 0, -6, -1])
# p3 = p1 + p2
# print p3.coeff #[1, 0, 0, 0, -6, -1]
# 
# p4 = p1*p2
# print p4.coeff #[0, 1, -1, 0, -6, 5, 1]
# 
#==============================================================================
p5 = p2.derivative()
print p5.coeff #[1, 0, 0, -24, -5]

#==============================================================================
# p = Polynomial ([1 , 2, 3])
# q = Polynomial ([2 , 3])
# r=p-q
# print r.coeff #[-1, -1, 3]
# 
# r=q-p
# print r.coeff #[1, 1, -3]
#==============================================================================
    