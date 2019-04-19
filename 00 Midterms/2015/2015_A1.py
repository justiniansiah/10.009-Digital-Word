import copy
a = [1, 2, [3, 4], 5]
b = a               #(i)
c = a[:]            #(ii)
d = copy.deepcopy(a)#(iii)

a[0] = 123123
a[2][0] = 123

print a
print b
print c
print d

# (i) b and a points to the same memory space (i.e a and b reference the same list)
# (ii) The nested list, [3,4] in a and c share the same memory space (i.e a and c reference the same nested list) BUT the remaining values occupy seperate spaces
# (iii) d is a full copy of a into another memory space so any edits to d, including the nested list, does not affect a