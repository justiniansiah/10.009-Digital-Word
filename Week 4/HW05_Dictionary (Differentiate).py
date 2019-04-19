def diff(p):
    der = {}
    for i, j in p.iteritems(): #<<< IMPT
        if i == 0:
            pass
        else:
            power = i-1
            var = i*j
            der.update({power:var})
    return der
    
    
print diff({0:-3, 3:2, 5:-1}) #{2: 6, 4: -5}
print diff({1:-3, 3:2, 5:-1, 6:2}) #{0:-3, 2:6, 4:-5, 5:12}
print diff({0:-3, 3:2, 8:2}) #{2:6, 7:16}
print diff({0:-4, 2:12, 3:-2, 4:3, 8:2}) #{1:24, 2:-6, 3:12, 7:16}
print diff({0:-3, 1:12, 2:-2, 3:2, 10:2}) #{0:12, 1:-4, 2:6, 9:20}