import random
from random import randint as rand
import time
random.seed(round(time.time()/3,-1))   #do not seed elsewhere in your code

def throw_dice(dice, exp):
    store = []
    for i in range(exp):
        dice_val=[]
        
        for j in range(dice): #rolling die
            dice_val.append(rand(1,6))
            checksum = 0
            
        for j in range(dice): #checking die 
            if dice_val[j] == 6:
                store.append(6)
                checksum = 1
                break
            if j == dice-1 and checksum == 0:
                store.append(1)
                
            
    
    six = 0.0
    for i in range(exp):
        if store[i] == 6:
            six += 1
    
    return round(six/exp,2)
    
    

print throw_dice(1,100000) #0.17
print throw_dice(1,200000) #0.17
print throw_dice(1,300000) #0.17
print throw_dice(2,500000) #0.31
print throw_dice(2,600000) #0.31


    
        
    