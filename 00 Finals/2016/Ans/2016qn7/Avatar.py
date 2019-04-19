class Avatar:
	def __init__(self, name, hp=100, position=(1,1)):
		self.name = name
		self.hp = hp
		self.position = position
	
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	
	def getHP(self):
		return self.hp
	def setHP(self, hp):
		self.hp = hp
	
	def getPosition(self):
		return self.position
	def setPosition(self, position):
		self.position = position
	
	def heal(self, amount=1):
		if amount > 0:
			self.hp += amount
	
	def attacked(self, damage=-1):
		if damage < 0:
			self.hp += damage
