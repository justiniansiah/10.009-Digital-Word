def move_disks(n, fromTower, toTower, auxTower, sol):
    if n >= 1:
        move_disks(n-1,fromTower,auxTower,toTower,sol)
        write(n,fromTower,toTower, sol)
        move_disks(n-1,auxTower,toTower,fromTower,sol)
    return sol

def write(n,fromT,toT,sol):
    aaa = 'Move disk %d from %s to %s' %(n,fromT,toT)
    sol.append(aaa)
    return

sol = []
n= 3
fromTower= 'A'
toTower= 'B'
auxTower= 'C'
print move_disks(n,fromTower,toTower,auxTower,sol)
    



