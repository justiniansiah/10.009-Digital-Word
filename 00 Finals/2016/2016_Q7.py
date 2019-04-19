from Avatar import Avatar
from Map import Map
import copy
from libdw import sm

class DW2Game(sm.SM):

    def __init__(self,avatar,map):
        avt = copy.deepcopy(avatar)
        mp = copy.deepcopy(map)
        self.startState = (avt,mp)       
        
    def getNextValues(self,state,inp):
        (cmd,dir) = inp
        (cavatar,cmap) = state
        avatar = copy.deepcopy(cavatar)
        map = copy.deepcopy(cmap)
        
        currLocation = avatar.position
        
        if dir == 'up':
            actiondir = (currLocation[0],currLocation[1]-1)
        elif dir =='down':
            actiondir = (currLocation[0],currLocation[1]+1)
        elif dir =='left':
            actiondir = (currLocation[0]-1,currLocation[1])
        elif dir =='right':
            actiondir = (currLocation[0]+1,currLocation[1])
        
        thing = map.whatIsAt(actiondir)
        if cmd == 'attack':
            attdmg = map.getEnemyAttack(actiondir)
            if attdmg == False:
                pass
            else:
                map.removeEnemy(actiondir)
                
           
        else: #move
            #empty space
            if thing == 'Empty' or thing == 'Exit':
                avatar.position = actiondir
            #food
            elif thing == 'Food':
                heal = map.getFoodEnergy(actiondir)
                avatar.heal(heal)
                avatar.position = actiondir
            #enemy
            elif thing == 'Enemy':
                dmg = map.getEnemyAttack(actiondir)
                avatar.attacked(dmg)
            #wall
            else:
                pass
        
        state = (avatar,map)
        output = (avatar.name,avatar.position,avatar.hp)
        return state,output
        
    def done(self,state):
        pos = state[0].position
        exit = state[1].getExitPosition()
        if pos == exit:
            return True
        else:
            return False            
            
            
        
        
        
        
        
        
world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0,(5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2):-2, (5,2): 0,(0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0,(1,5):0, (2,5):0, (3,5):0, (4,5):'x', (5,5): 0,}

#print 'test 1'
# inp=[('move','down'),('attack','down'),('move','down'),('move','down'),('move','down'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down')]
# av=Avatar('John')
# m=Map(world2)
# g=DW2Game(av,m)
# print g.transduce(inp)
#print '\n'

print 'test 2'
inp=[('move','left'),('move','right'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move','down'),('move','up')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)
print '\n'

print 'test 3'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)
print '\n'

print 'test 4'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),('move','right')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)
print '\n'

print 'test 5'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),
('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move','down')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print '\n'
print 'test 6'
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
g.start()
n,o=g.getNextValues(g.startState,('move','right'))
ans = g.state[0].getPosition() == n[0].getPosition()
print ans, g.state[0].getPosition(), n[0].getPosition()
