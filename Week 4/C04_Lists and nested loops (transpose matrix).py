import numpy
import copy

def transpose_matrix(list):
    trans = [[] for x in range(len(list[0]))] 
    
    for i in range (len(list[0])):
        inner = []
        for j in range (len(list)):
            inner.append(0)
        #print inner
        trans[i] = inner
    #print trans
            
    for i in range (len(list)):
       for j in range (len(list[i])):
           temp = list[i][j]
           trans[j][i] = temp  
    return trans
    
a = [[1 ,2 ,3] , [4 ,5 ,6] , [7 ,8 ,9]]
print transpose_matrix (a) #[[1 ,4 ,7] , [2 ,5 ,8] , [3 ,6 ,9]]

a = [[-11,12,3], [4,-5,6]]
print transpose_matrix (a) #[[-11, 4], [12, -5], [3, 6]]

a = [[1,2], [10,5], [0,0]]
print transpose_matrix (a) #[[1, 10, 0], [2, 5, 0]]