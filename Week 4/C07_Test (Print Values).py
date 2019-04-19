#Print "A" at multiples of 5, "B" at multiples of 7, "AB" at multiples of 5 and 7

def printvals(n):
    list = []
    for i in range(n):
        if (i+1)>1 and (i+1)%5 == 0 and (i+1)%7 ==0:
            list.append("AB")
        elif (i+1)%5 ==0:
            list.append("A")
        elif (i+1)%7 ==0:
            list.append("B")
        else:
            list.append(i+1)
    
        
    return list
    
    
print printvals(36)
        