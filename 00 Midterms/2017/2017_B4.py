#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def mysum(a,b,limit):
    if int(a) != a or int(b) != b:
        a = 0
    if str(a).isalpha() or str(b).isalpha() or a<=0  or b<=0:
        summ = "Wrong input"

    else:
    
        no = 0
        count= 1
        list = []
        while no < limit:
            powera = a**count
            powerb = b**count
            aa = a*count
            bb = b*count
            temp = [powera,powerb,aa,bb]
            
            if powera < limit and powera not in list:
                list.append(powera)
            if powerb < limit and powerb not in list:    
                list.append(powerb)
            if aa < limit and aa not in list:    
                list.append(aa)
            if bb < limit and bb not in list:    
                list.append(bb)
            
            count += 1
            no = min(temp)
        
        summ = sum(list)
    
        
        
    return summ
    

print mysum(3,5,10) #23
# print mysum(2,4,12) #30
# print mysum(3,3,15) #30
# print mysum(7,9,100) #30
# print mysum(21,34,10000) #3783486
# print mysum(0,5,10) #Wrong Input
print mysum(0.5,5,10) #Wrong Input
#print mysum(3,'x',10) #Wrong Input
#print mysum(2,3,0) #0

