def may_ignore(arg):
    if type(arg) == type(1):
        return arg+1
    else:
        print type(arg)
        return "None"
    
print may_ignore(1)
print may_ignore(1.0)
print may_ignore(1+2j)
print may_ignore("Hello")
