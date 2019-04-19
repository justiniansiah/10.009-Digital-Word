from cmath import sqrt as sqrt
def norm(z1,z2,z3):
    z = sqrt(z1*z1.conjugate()+z2*z2.conjugate()+z3*z3.conjugate())
    return round(z.real,3)
    
z1 = 1+3j
z2 = -1+3j
z3= -1-3j

print norm(z1,z2,z3) #5.477

z1=1+2j
z2=-1+2j
z3=-1-2j

print norm(z1,z2,z3) #3.873

z1=1+1j
z2=-1+1j
z3=-1-1j

print norm(z1,z2,z3) #2.449
