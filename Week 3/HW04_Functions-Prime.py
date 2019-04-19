def is_prime(no):
    if no <=1:
        return False
    elif no == 2:
        return True
    else:
        for i in range (2,no):
            if no%i == 0:
                return False
        return True

print is_prime(2)
print is_prime(3)
print is_prime(7)
print is_prime(9)
print is_prime(21)
print is_prime(0)