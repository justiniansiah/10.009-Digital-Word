import random

craps = set ([2 ,3 ,12])
naturals = set ([7 ,11])

def roll_two_dices():
    return random.randint(1,6),random.randint(1,6)

def print_lose():
    print "You lose"
    return

def print_win():
    print "You win"
    return

def print_point(p):
    print "Your points are %d" %(p)
    return

def is_craps(n):
    if n == 2 or n == 3 or n == 12:
        return True
    else:
        return False

def is_naturals(n):
    if n == 7 or n == 1:
        return True
    else:
        return False

def play_craps():
    point =-1
    
    while True :
        n1,n2 = roll_two_dices()
        sumn =n1+n2
        print 'You rolled %d + %d = %d'%(n1 ,n2 , sumn )
        
        if point == -1:
            if is_craps(sumn):
                print_lose()
                return 0
            elif is_naturals(sumn):
                print_win()
                return 1
            
            point = sumn
            print_point(point)
        
        else:
            if sumn == 7:
                print_lose()
                return 0
            elif sumn == point :
                print_win()
                return 1
                
play_craps()