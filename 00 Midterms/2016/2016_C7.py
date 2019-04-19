# def maxProductThree(num):
#     negatives = 0
#     for i in num:
#         if i<0:
#             negatives+=1
#     if negatives <2:
#         L1=0
#         L2=0
#         L3=0
#         for i in num:
#             if i>0 and i > L1:
#                 L1 = i
#         for i in num:
#             if i>0 and i != L1 and i > L2:
#                 L2 = i
#         for i in num:
#             if i>0 and i != L1 and i != L2 and i > L3:
#                 L3 = i
#         ans = L1*L2*L3
#     
#     else:
#         neg = []
#         pos = []
#         for i in num:
#             if i<0:
#                 neg.append(i)
#             elif i>0:
#                 pos.append(i)
#         
#         
# 
#     return        
             
def maxProductThree(num):
    nz = []
    for i in num:
        if i != 0:
            nz.append(i)      
    maxlist =[]   
    for i in range(len(nz)):
        for j in range(i+1,len(nz)):
            for h in range(j+1,len(nz)):
                maxlist.append(nz[i]*nz[j]*nz[h])
    return max(maxlist)
        
  
    
num=[6,-3,-10,0,2]
print maxProductThree(num) #180

num=[1,2,3,4,5,6,-7,-8]
print maxProductThree(num) #180