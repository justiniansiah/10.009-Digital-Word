from libdw import sm

class RingCounter(sm.SM):
	startState = 0
	
	def getNextValues(self, state, inp):
		if inp == 0:
			state = (state + 1) % 8
		else:
			state = 0
		return (state, '{0:03b}'.format(state))

print 'test 1'
r=RingCounter()
print r.transduce([0,0,0,0,0,0,0,0,0])

print 'test 2'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,0,0,0])

print 'test 3'
r=RingCounter()
print r.transduce([0,0,0,1,0,0,1,0,0])
