def check_value(n1,n2,n3,x):
    if x > n1 and x > n2 and x < n3:
        return True
    else:
        return False
        
print check_value(1,4,8,7)
print check_value(10,4,8,7)
print check_value(1,10,8,7)
print check_value(1,4,5,7)
    