import copy
def readMatrix(f):
    dict = {}
    key = ["matrix","op"]
    count = -1
    for i in f:
        x = i.strip()
        if x.isalpha():
            count += 1
            list = []
        else:
            list2 = []
            y = x.split()
            for i in y:
                if count == 0:              #because matrix is float
                    list2.append(float(i))
                else:                        #because op is string
                    list2.append(i)
            list.append(list2)    
            dict[key[count]] = list            
    return dict  
            
    
def mulRowByC(matOp,i,c):
    for j in range(len(matOp[i])):
        matOp[i][j]*=c
        matOp[i][j]= round(matOp[i][j],2)
    return matOp
    
# A=[[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# print mulRowByC(A,0,2)    
    
def addRowMulByC(matOp,i,c,j):
    for h in range(len(matOp[i])):
        matOp[j][h]+=(matOp[i][h]*c)
        matOp[j][h] = round(matOp[j][h],2)
    return matOp
    
# A=[[0,2,1,-1],[0,0,3,1],[0,0,0,0]]
# print addRowMulByC(A,0,0.5,1)     
    
    
def gaussElimination(data):
    matOp= copy.deepcopy(data["matrix"])
    for a in data["op"]:
        if a[0] == '1':
            i = int(a[1])
            c = float(a[2])
            matOp = mulRowByC(matOp,i,c)
        if a[0] == '2':
            i = int(a[1])
            c = float(a[2])
            j = int(a[3])
            matOp = addRowMulByC(matOp,i,c,j)
            
    return data["matrix"],matOp

def test():    
    f = open('gauss2.txt','r')
    dict = readMatrix(f)
    f.close()
    matA, result=gaussElimination(dict)
    print matA
    print result  
    
test()

