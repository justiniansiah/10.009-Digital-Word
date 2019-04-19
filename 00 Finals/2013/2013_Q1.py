def init():
    return [[ '_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def show(grid):
    out = ''
    for i in range (3):
        for j in range(3):
            out+= grid[i][j]
        out+='\n'
    return out

def movex(b,i,j):
    for q in range (3):
        for w in range (3):
            if q == i-1 and w == j-1:
                b[q][w] = 'x'
            

def moveo(b,i,j):
    for q in range (3):
        for w in range (3):
            if q == i-1 and w == j-1:
                b[q][w] = 'o'

def countmoves(grid):
    count = 0
    for q in range (3):
        for w in range (3):
            if grid[q][w] != '_':
                count +=1
    return count
    
def getmoves(grid):
    x = []
    o = []
    for q in range (3):
        for w in range (3):
            if grid[q][w] == 'x':
                x.append((q+1,w+1))
            elif grid[q][w] == 'o':
                o.append((q+1,w+1))
    return {'x':x,'o':o}

def winsx(grid):
    for i in range (3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 'x':
            return True
        elif grid[0][i] == grid[1][i] == grid[2][i] == 'x':
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == 'x':
        return True
    elif grid[0][2] == grid[1][1] == grid[2][0] == 'x':
        return True
    else:
        return False 

def winso(grid):
    for i in range (3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 'o':
            return True
        elif grid[0][i] == grid[1][i] == grid[2][i] == 'o':
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == 'o':
        return True
    elif grid[0][2] == grid[1][1] == grid[2][0] == 'o':
        return True
    else:
        return False        
            

b = init()
b = [[ 'x', 'o', '_'],['_', 'o', 'x'],['_', '_', 'x']]
print show(b)
#movex(b,1,3)
print show(b)
print countmoves(b)
print getmoves(b)
print winsx(b)
