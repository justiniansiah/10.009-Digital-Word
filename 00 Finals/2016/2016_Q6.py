import copy 

class Map(object):
    def __init__(self,mapInfo):
        self.world = copy.deepcopy(mapInfo)
        #>0 : food energy 
        #<0 : attack value
        # 0 : wall
        # x : exit point
        
    def whatIsAt(self,(x,y)):
        if (x,y) in self.world:
            result = self.world[(x,y)]
            if result == 'x':
                result = 'Exit'
            elif result < 0:
                result = 'Enemy'
            elif result == 0:
                result = 'Wall'
            elif result > 0:
                result = 'Food'
        else:
            result = 'Empty'
        return result
        
    def getEnemyAttack(self,(x,y)):
        if (x,y) in self.world:
            dmg = self.world[(x,y)]
            if dmg < 0:
                return dmg
            else:
                return False
        else:
            dmg = False
        return dmg
        
    def getFoodEnergy(self,(x,y)):
        if (x,y) in self.world:
            heal = self.world[(x,y)]
            if heal > 0:
                if heal != 'x':
                    return heal
                else:
                    return False                    
            else:
                return False
        else:
            heal = False
        return heal
        
    def removeEnemy(self,(x,y)):
        if (x,y) in self.world:
            rem = self.world[(x,y)]
            if rem < 0:
                del self.world[(x,y)]
                return True
            else:
                return False
        else:
            rem = False
        return rem
        
    def getExitPosition(self):
        if 'x' in self.world.values():
            for i in self.world:
                if self.world[i] == 'x':
                    return i
        else:
            return None
        
    def eatFood(self,(x,y)):
        if (x,y) in self.world:
            heal = self.world[(x,y)]
            if heal > 0:
                if heal != 'x':
                    del self.world[(x,y)]
                    return True
                else:
                    return False                    
            else:
                return False
        else:
            heal = False
        return heal
        
        
        
        
        
        
world = {(0,0):0, (1,0):0,(2,0):0,(3,0):0,(4,0):0,(5,0):0,(0,1):0,(1,1):2,(2,1):-3,(5,1):0,(0,2):0,(5,2):0,(0,3):0,(5,3):0,(0,4):0,(5,4):0,(0,5):0,(1,5):0,(2,5):0,(3,5):0,(4,5):'x',(5,5):0}

print 'test 1: Object instantitiation'
m = Map(world)
print m.world
print '\n'

print 'test 2: whatIsAt'
print m.whatIsAt((1,0)) #Wall
print m.whatIsAt((2,1)) #Enemy
print m.whatIsAt((1,1)) #Food
print m.whatIsAt((4,5)) #Exit
print '\n'

print 'test 5: getEnemyAttack'
print m.getEnemyAttack((1,0))
print m.getEnemyAttack((2,1)) #-3
print m.getEnemyAttack((1,1))
print m.getEnemyAttack((4,5))
print '\n'

print 'test 6: getFoodEnergy'
print m.getFoodEnergy((1,0))
print m.getFoodEnergy((2,1)) 
print m.getFoodEnergy((1,1)) #2
print m.getFoodEnergy((4,5))
print '\n'

print 'test 7: removeEnemy'
w1 = m.getEnemyAttack((2,1))
w2 = m.removeEnemy((2,1))
w3 = m.getEnemyAttack((2,1))
print (w1,w2,w3) #(-3,True,False)
print '\n'

print 'test 8: whatIsAt'
print m.whatIsAt((1,4)) #Empty
print '\n'

print 'test 9: getFoodEnergy'
print m.getFoodEnergy((1,4)) #False
print '\n'

print 'test 10: getEnemyAttack'
print m.getEnemyAttack((1,4)) #False
print '\n'

print 'test 11: whatIsAt'
print m.whatIsAt((4,5)) #Exit
print '\n'

print 'test 12: getExitPosition'
print m.getExitPosition() #Exit
print '\n'

print 'test 13: eatFood'
w1 = m.whatIsAt((1,1))
w2 = m.eatFood((1,1))
w3 = m.whatIsAt((1,1))
print (w1,w2,w3) #(Food,True,Empty)
print '\n'

print 'test 14: test aliasing'
print m.world == world