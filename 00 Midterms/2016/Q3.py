import cmath
def norm(z1,z2,z3):
    z1 = combine(z1)
    z2 = combine(z2)
    z3 = combine(z3)
    Z = z1+z2+z3
    sq = cmath.sqrt(Z)
    
    return round(sq.real,3)

def combine(zi):
    czi = zi.conjugate()
    zzi = zi*czi
    return zzi
    
z1 = 1+3j
z2 = -1+3j
z3 = -1-3j

print norm(z1,z2,z3)
