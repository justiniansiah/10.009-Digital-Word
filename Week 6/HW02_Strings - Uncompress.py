def uncompressed(s):
    S = list(s)
    string = ""
    for i in S:
        if i.isdigit():
            num = int(i)
        else:
            for j in range(num):
                string += i
    return string

print uncompressed("2a5b1c") #aabbbbbc
print uncompressed("1a1b2c") #abcc
print uncompressed("1a9b3b1c") #abbbbbbbbbbbbc

    
    
