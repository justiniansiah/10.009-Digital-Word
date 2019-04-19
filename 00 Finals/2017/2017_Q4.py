def get_products(inlist, test):
    pdt = {}
    for i in inlist:
        pro = 1
        for j in range(len(i)):
            pro *= i[j]
        if pro not in pdt:
            
            pdt[pro]=[i]
        else:
            pdt[pro].append(i)
    if test in pdt.keys():
        out = pdt[test]
    else:
        out = None
    return pdt,out
    







inlist = [(3,5),(2,2),(2,2,3),(12,2),(7,3),(3,7,1)]

d,o = get_products(inlist, 15) 
print sorted(d.keys()) #[4, 12, 15, 21, 24]
print sorted(d.values()) #[[(2, 2)], [(2, 2, 3)], [(3, 5)], [(7, 3), (3, 7, 1)], [(12, 2)]]
print o  #[(3, 5)]

d,o = get_products(inlist, 21) 
print o #[(7, 3), (3, 7, 1)]

d,o = get_products(inlist, 11) 
print o #None