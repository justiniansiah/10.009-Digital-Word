
def complete_ISBN(ins):
    d =[]
    for i in range(9):
        d.append(int(ins[i]))
        checksum =0
    for i in range(9):
        checksum+= d[i]*(i+1)
    
    checksum %= 11
    if checksum == 10:
        checksum = 'X'
        
    string = ''
    for i in range(9):
        string += str(d[i])
        
    string += str(checksum)
    return string
        
    
    
    
print 'Test case 1: ins=013601267'
print complete_ISBN('013601267') #0136012671

print 'Test case 2: ins=013031997'
print complete_ISBN('013031997') #013031997X

print 'Test case 3: ins=020139829'
print complete_ISBN('020139829') #020139829X



