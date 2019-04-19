n1 = int(raw_input("N1: "))
n2 = int(raw_input("N2: "))

out = []
if (n1)%2 == 0: #n1 is even
    a = n1+1
    while a <= n2:
        out.append(a)
        a+=2
        
else: #n1 is odd
    while n1<=n2:
        out.append(n1)
        n1+=2

print out
