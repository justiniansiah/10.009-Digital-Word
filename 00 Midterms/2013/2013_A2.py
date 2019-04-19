def findKey(d,s):
    for i in d:
        if str(i) in s:
            return True
    return False
        
d={1:'Tokyo', 2:'Qatar', 3:'Singapore'}
s='KL'
print findKey(d,s)