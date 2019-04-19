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
