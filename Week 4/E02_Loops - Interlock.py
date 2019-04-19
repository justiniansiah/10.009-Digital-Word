def interlock(word1,word2,word3):
    list1=list(word1)
    list2=list(word2)
    list3=list(word3)
    
    if len(list3)==0:
        return False
        
    if len(list1) + len(list2) == len(list3):
        j = 0
        for i in range(0,len(list3),2):
            if list1[j] == list3[i]:
                pass
            else: 
                return False
            j +=1
            
        j = 0        
        for i in range(1,len(list3),2):
            if list2[j] == list3[i]:
                pass                
            else: 
                return False
            j +=1 
            
            
    else:
        return False
    
    
    return True

print interlock('shoe','cold','schooled')
print interlock('shoes','cold','schooled')
print interlock('','cold','schooled')
print interlock('shoes','cold','')
print interlock('','','')
print interlock('can','his','chains')