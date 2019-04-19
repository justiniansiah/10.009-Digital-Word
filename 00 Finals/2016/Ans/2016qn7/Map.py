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
			heal = copy.copy(self.world[position])
			del self.world[position]
			return heal
		return False
	
	def getExitPosition(self):
		for k, v in self.world.iteritems():
			if v == 'x':
				return k
