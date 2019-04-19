def max_list(inp):
    out = []
    for i in range(len(inp)):
        out.append(max(inp[i]))
    return out    
    
    
    
print max_list([[1,2,3],[4,5]]) #[3, 5]
print max_list([[1,2,3],[4,5],[32,3,4]]) #[3, 5, 32]
print max_list([[3,4,5,2],[1,7],[8,0,-1],[2]]) #[5, 7, 8, 2]
print max_list([[100],[1,7],[-8,-2,-1],[2]]) #[100 , 7, -1, 2]
print max_list([[3,4,5,2]]) #[5]