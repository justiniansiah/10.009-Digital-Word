def find_average(list):
    lengthtotal=len(list)
    out = []
    supersum = 0.0
    elementcount = 0.0
    
    for i in range(lengthtotal):
        sum = 0.0
        
        for j in range(len(list[i])):
            sum += list[i][j]
            supersum += list[i][j]
            elementcount +=1
        if len(list[i]) == 0:
            sum = 0.0
        else:
            sum = sum/len(list[i])
        out.append(sum)
        
    sum = 0.0
    
    for i in range(lengthtotal):
        sum += out[i]
        
    if elementcount == 0:
        avg = 0.0
    else:
        avg = supersum/elementcount
    ans = (out,avg)

    return ans
    
print find_average ([[3 ,4] ,[5 ,6 ,7] ,[ -1 ,2 ,8]]) #([3.5 , 6.0 , 3.0] , 4.25)
print find_average ([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]]) #([5.11 , 0.0 , 0.89] , 3.0)
print find_average ([[3.6] ,[1 ,2 ,3] ,[1 ,1 ,1]]) #([3.6 , 2.0 , 1.0] , 1.8)
print find_average ([[2 ,3 ,4] ,[2 ,6 ,7] ,[10 ,5 ,15]]) #([3.0 , 5.0 , 10.0] , 6.0)
