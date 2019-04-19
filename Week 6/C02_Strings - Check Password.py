# A password must have at least 8 characters.
# A password must consist of only letters and digits.
# A password must contain at least two digits.

def check_password(password):
    digit = 0
    if len(password) >= 8 and password.isalnum():
        for i in password:
            if i.isdigit():
                digit += 1
        if digit >= 2:
            return True
    else:
        return False
    return False
    
print check_password("test") #False
print check_password("testtest") #False
print check_password("testt22") #False
print check_password("testte22") #True