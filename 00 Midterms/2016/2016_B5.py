def combinations(n1,n2):
    ans = []

    for i in range (n1,n2+1):
        for j in range (i+1,n2+1):
            ans.append((i,j))
    return (ans,len(ans))
    
print combinations(1,7)
print combinations(3,5)
print combinations(-1,2)
print combinations(0,0)