#### Pay 1 dollar throw 4 die, if eye < 9 you win $r. If r = 10 should you play?
import math
import random
import time
random.seed(round(time.time()/3,-1)) #do not seed elsewhere in your code

def game(r,exp):
    spent = 0
    earned = 0
    
    while exp>0:        
        dice = []
        spent += 1
        
        for i in range(4):
            dice.append(random.randint(1,6))
        if sum(dice) < 9:
            earned += r
        
        
        exp -= 1
        print earned
        if earned - spent < 0:
            return False
        elif earned - spent >= 0:
            return True
    return
    
print game(100,100)
    