def maxOccurrences(inp):
    a = inp.split()
    dict = {}
    for i in range(len(a)):
        #a[i] = int(a[i])
        no = int(a[i])
        if no not in dict:
            dict[no]=1
        else:
            dict[no]+=1
    lst = []
    for i in dict:        
        if dict[i] == max(dict.values()):
            lst.append(i)   
    lst.sort()    
    
    return (lst,max(dict.values()))    



print 'test 1'
inp = '2 3 40 3 5 4 -3 3 3 2 0'
print maxOccurrences(inp) #([3],4)

print 'test 2'
inp = '9 30 3 9 3 2 4'
print maxOccurrences(inp) #([3,9],2)