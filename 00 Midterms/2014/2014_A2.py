def sumVal(d):
    a=0
    if len(d)== 0:
        return None
    else:
        for i in d:
            if i<3:
                a+= d[i]
    return a

d={4:-7, 8: 4, 2: 10, 1: -2}
d= {}
print sumVal(d)
    
    