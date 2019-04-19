# def binary_to_decimal(binaryStr):
#     return int(binaryStr,2)

def reverse(s):
    return s[::-1]

def binary_to_decimal(binaryStr):
    bins = reverse(binaryStr)
    AAA = list(bins)

    ans = 0
    for i in range(len(AAA)):
        if AAA[i] == "1":
            ans += (2**i)
    return ans
    
    
print binary_to_decimal("100") #4
print binary_to_decimal("101") #5
print binary_to_decimal("10001") #17
print binary_to_decimal("10101") #21


    
    
