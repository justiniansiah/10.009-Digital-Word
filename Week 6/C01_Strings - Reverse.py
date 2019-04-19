# def reverse(s):
#     return s[::-1]

def reverse(s):
    out = ""
    for i in range(len(s)):
        out += s[-i-1]
    
    return out
        

print reverse("I am testing") #gnitset ma I
print reverse("ABCDEFGHIJK") #KJIHGFEDCBA