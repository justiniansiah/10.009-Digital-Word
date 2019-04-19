def gcd(n1,n2):
    gcd = 1
    if n1>n2:
        x = n2
    elif n2>n1:
        x = n1
    else:
        return n1
    for i in range(1,x+1):
        if n2%i == 0 and n1%i == 0:
            gcd = i
                             
    return gcd

print gcd(54,24)
print gcd(20,10)
print gcd(42,30)

