def maxOccurrences(inp):
	d = dict()
	for i in inp.split():
		if i not in d.keys():
			d[i] = 0
		d[i] += 1
	
	maxCount = -1
	
	for v in d.values():
		if v > maxCount:
			maxCount = v
	
	maxList = list()
		
	for k in d.keys():
		if d[k] == maxCount:
			maxList.append(int(k))
	return (sorted(maxList), maxCount)

print 'test 1'
inp='2 3 40 3 5 4 -3 3 3 2 0'
print maxOccurrences(inp)

print 'test 2'
inp='9 30 3 9 3 2 4'
print maxOccurrences(inp)
