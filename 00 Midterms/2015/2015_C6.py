def getSchedule(f):
    dict = {}
    temp = []
    check = 0
    for i in f:
        if check == 0:
            storeday = i.strip()
            check = 1
            
        s1 = i.strip()
        s2 = s1.split()
        if s2[0].isdigit():
            temp.append((int(s2[0]),int(s2[1])))
            check = 2
        elif check == 2:
            dict[storeday]=temp
            temp = []
            storeday = i.strip()
            check = 1
    dict[storeday]=temp #added this to include last day of file        
    return  dict      
    
    
def findLength(dictSchedule):
    dict = {}
    for i in dictSchedule:
        sum = 0
        temp = dictSchedule[i]
        for j in range(len(temp)):
            sum += (temp[j][1] - temp [j][0])
        dict[i]=sum
            
    return dict
    
    
def findConflict(dictSchedule):
    dict = {}
    for i in dictSchedule:
        temp = dictSchedule[i]
        temp2 =[]
        out = False
        for j in range(len(temp)):
            temp3 = range(temp[j][0]+1,temp[j][1])
            for k in range(j+1,len(temp)):
                if temp[k][0] in temp3 or temp[k][1] in temp3:
                    out = True
            dict[i]= out
    return dict
    
    
f = open('test.txt','r')
dict = getSchedule(f)
#print findLength(dict)
print findConflict(dict)