# Recursion: Write a function named factorial that takes in a number n and returns its
# factorial. You can solve this problem either using loops or recursion. Note that 0! = 1,
# and n! = n x (n-1)! for n > 0.

def factorial(n):
    if n == 0:
        return 1
    else:
        asdf = 1
        for i in range(1,n+1):
            asdf *= i
    return asdf

print factorial(0) #1
print factorial(1) #1
print factorial(2) #2
print factorial(5) #120
print factorial(10)#362880
        



