def genList(n1,n2):
    out = []
    for i in range(n1,n2+1):
        if i%3 == 0:
            out.append(i)
            
    return out

print genList(2,12)
print genList(2,20)