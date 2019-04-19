def findKey(dict,str):
    out = []
    for i in dict:
        if dict[i] == str:
            out.append(i)
    out.sort()
    return out
        
    
    
dInput = {1:'singapore', 20:'china', 4:'japan', 5:'china', 10:'japan'}
print findKey(dInput, 'china') #returns [5, 20]
print findKey(dInput, 'korea') #returns []