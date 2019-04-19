def check(s,n):
    if s.isdigit():
        return n+int(s)
    else:
        return n
    
s = '12'
n = 9

# s = 'hello'
# n = 10

print check(s,n)