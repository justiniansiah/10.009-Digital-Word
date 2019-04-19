import copy

class Map:
	def __init__(self, world):
		self.world = copy.deepcopy(world)
	
	def whatIsAt(self, position):
		if position not in self.world.keys():
			return 'Empty'
		elif self.world[position] == 0:
			return 'Wall'
		elif self.world[position] == 'x':
			return 'Exit'
		elif self.world[position] > 0:
			return 'Food'
		elif self.world[position] < 0:
			return 'Enemy'
	
	def getEnemyAttack(self, position):
		if self.whatIsAt(position) == 'Enemy':
			return self.world[position]
		return False
	
	def getFoodEnergy(self, position):
		if self.whatIsAt(position) == 'Food':
			return self.world[position]
		return False
	
	def removeEnemy(self, position):
		if self.whatIsAt(position) == 'Enemy':
			del self.world[position]
			return True
		return False
	
	def eatFood(self, position):
		if self.whatIsAt(position) == 'Food':
			del self.world[position]
			return True
		return False
	
	def getExitPosition(self):
		for k, v in self.world.iteritems():
			if v == 'x':
				return k

world={(0,0):0, (1,0):0 , (2,0):0, (3,0): 0, (4,0):0, (5,0): 0, (0,1):0, (1,1): 2, (2,1):-3, (5,1): 0, (0,2):0, (5,2): 0, (0,3):0, (5,3): 0, (0,4):0, (5,4): 0, (0,5):0, (1,5):0 , (2,5):0, (3,5): 0, (4,5):'x', (5,5): 0}

print 'test 1: object instantiation'
m=Map(world)
print m.world

print 'test 2: whatIsAt'
print m.whatIsAt((1,0))

print 'test 3: whatIsAt'
print m.whatIsAt((2,1))

print 'test 4: whatIsAt'
print m.whatIsAt((1,1))

print 'test 5: getFoodEnergy'
w1=m.getFoodEnergy((1,1))
w2=m.getFoodEnergy((3,3))
print (w1,w2)

print 'test 6: getEnemyAttack'
w1=m.getEnemyAttack((2,1))
w2=m.getEnemyAttack((3,3))
print (w1,w2)

print 'test 7: removeEnemy'
w1=m.getEnemyAttack((2,1))
w2=m.removeEnemy((2,1))
w3=m.getEnemyAttack((2,1))
print (w1,w2,w3)

print 'test 8: whatIsAt'
print m.whatIsAt((1,4))

print 'test 9: getFoodEnergy'
print m.getFoodEnergy((1,4))

print 'test 10: getEnemyAttack'
print m.getEnemyAttack((1,4))

print 'test 11: whatIsAt'
print m.whatIsAt((4,5))

print 'test 12: getExitPosition'
print m.getExitPosition()

print 'test 13: eatFood'
w1=m.whatIsAt((1,1))
w2=m.eatFood((1,1))
w3=m.whatIsAt((1,1))
print (w1,w2,w3)

print 'test 14: test aliasing'
print m.world == world
