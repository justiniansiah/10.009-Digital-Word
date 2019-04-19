from libdw import sm
from Avatar import Avatar
from Map import Map
import copy

class DW2Game(sm.SM):
	DIRECTIONS = {'up':(0, -1), 'down':(0, 1), 'left':(-1, 0), 'right':(1, 0)}
	
	def __init__(self, a, m):
		self.startState = (copy.deepcopy(a), copy.deepcopy(m))
	
	def getNextValues(self, state, inp):
		a = copy.deepcopy(state[0])
		m = copy.deepcopy(state[1])
		if inp[0] == 'move':
			newPosition = (a.getPosition()[0] + DW2Game.DIRECTIONS[inp[1].strip()][0], a.getPosition()[1] + DW2Game.DIRECTIONS[inp[1].strip()][1])
			
			if m.whatIsAt(newPosition) == 'Food':
				a.setPosition(newPosition)
				a.heal(m.eatFood(newPosition))
			elif m.whatIsAt(newPosition) == 'Empty' or m.whatIsAt(newPosition) == 'Exit':
				a.setPosition(newPosition)
			elif m.whatIsAt(newPosition) == 'Enemy':
				a.attacked(m.getEnemyAttack(newPosition))
		elif inp[0] == 'attack':
			attackPosition = (a.getPosition()[0] + DW2Game.DIRECTIONS[inp[1].strip()][0], a.getPosition()[1] + DW2Game.DIRECTIONS[inp[1].strip()][1])
			m.removeEnemy(attackPosition)
		
		return (a, m), (a.getName(), a.getPosition(), a.getHP())
	
	def done(self, state):
		a = copy.deepcopy(state[0])
		m = copy.deepcopy(state[1])
		if a.getPosition() == m.getExitPosition():
			return True
		return False

world2={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (5,1): 0, (0,2):0, (1,2): -2, (5,2): 0, (0,3):0, (2,3): 3, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0, (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}

print 'test 1'
inp=[('move','down'),('attack','down'),('move','down'),('move','down'),('move','down'),('move','right'),('move','right'),('move',' right'),('move','down'),('move','down')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print 'test 2'
inp=[('move','left'),('move','right'),('move','right'),('move','right'),('move','right'),('move','down'),('move','down'),('move' ,'down'),('move','up')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print 'test 3'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print 'test 4'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),('move','right')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print 'test 5'
inp=[('move','right'),('move','right'),('move','right'),('move','down'),('move','left'),('move','left'),('move','left'),('attack','left'),('move','left'),('move','left'),('move','down'),('move','right'),('move','right'),('move','right'),('move',' down'),('move','down'),('move','down')]
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
print g.transduce(inp)

print 'test 6'
av=Avatar('John')
m=Map(world2)
g=DW2Game(av,m)
g.start()
n,o=g.getNextValues(g.startState,('move','right'))
ans = g.state[0].getPosition() == n[0].getPosition()
print ans, g.state[0].getPosition(), n[0].getPosition()
