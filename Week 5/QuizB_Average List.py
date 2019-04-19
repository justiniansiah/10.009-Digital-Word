def average_list(inp):
    out = []
    for i in range (len(inp)):
        out.append(list_avg(inp[i]))
    return out

def list_avg(list):
    ans = 0
    for i in range (len(list)):
        ans += list[i]
    return ans/(len(list))


# def average_list(list):
#     a = []
#     for h in range (len(list)):
#         b = 0
#         for i in range (len(list[h])):
#             b += list[h][i]
#             b /= len(list[i])            
#         a.append(b)
#     return a
    
list = [[100],[1,7],[8,0,-1],[2]] 
print average_list(list) #[100,4,2,2]