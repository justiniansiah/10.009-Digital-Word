def compTrace(A):
    out = 0
    for i in range(len(A)):
        out += A[i][i]
    return out
    
A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
print compTrace(A) #16.2