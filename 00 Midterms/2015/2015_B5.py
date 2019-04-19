def matAdd(A,B):
    C = []
    for i in range(len(A)):
        C1 =[]
        for j in range(len(A[0])):
            C1.append (A[i][j] + B[i][j])
        C.append(C1)
    return C
    


A = [[1,2,3], [4, 5, 6]]
B = [[10,20,30], [40, 50, 60]]
C = matAdd(A,B)
print 'A:', A, 'B:', B, 'C:', C