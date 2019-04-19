# def list_sum(list):
#     ans = 0.0
#     for i in range (len(list)):
#         ans += list[i]
#     return ans

def list_sum(list):
    return sum(list)
    
print ( "Test case 1: [4.25 ,5.0 ,10.75]" )
print list_sum ([4.25 ,5.0 ,10.75])

print ("Test case 2: [5.0] ")
print list_sum ([5.0])

print ( "Test case 3: [] " )
print list_sum ([])

