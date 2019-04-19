

def countNumOpenLocker(K):
    locker = []
    for i in range(K):
        locker.append('o')
    for i in range(2,K+1):
        for j in range(i-1,K,i):
            #print j
            if locker[j] == 'c':
                locker[j] = 'o'
            else:
                locker[j] = 'c'
            # print locker
        # print i
    
    no = 0
    for i in range(K):
        if locker[i] == 'o':
            no +=1
    return no
                
#print countNumOpenLocker(2000) #44
# N = 26
# for i in range(N):
#     print countNumOpenLocker(i)
    
#0:1 
#1:3 3:5 4:7 5:9 6:11  7:13 8:15

N = 44 #ie btwen 1936 and 2025, 44 doors are open
#N = 1000 #hence when 1000 doors are open,  K = 1000000 onwards
ans = 0
for n in range(N):
    ans += (2*n)+1
print ans



