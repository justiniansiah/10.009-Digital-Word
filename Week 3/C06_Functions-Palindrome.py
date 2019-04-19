def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
        
        
        
print ( "Test case 1: 1" )
print is_palindrome (1)

print ( "Test case 2: 22" )
print is_palindrome (22)

print ( "Test case 3: 12321" )
print is_palindrome (12321)

print ( "Test case 4: 441232144" )
print is_palindrome (441232144)

print ( "Test case 5: 441231144" )
print is_palindrome (441231144)

print ( "Test case 6: 144" )
print is_palindrome (144)

print ( "Test case 7: 12" )
print is_palindrome (12)