def fib(no): #fibbonaci
    s = 0
    n = 1
    if no == 1 or no == 2:
        return 1
    else:
        for i in range (1,no):
            o=n
            n+=s
            s=o
    
    return n
    
ans = fib (1000)
print (ans)