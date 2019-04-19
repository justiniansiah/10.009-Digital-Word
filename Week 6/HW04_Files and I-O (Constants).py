def get_fundamental_constants(f):
    dict = {}
    start = 0
    for i in f:
        line = i.strip()
        LINE = line.split()
        if start >1:
            dict[LINE[0]] = float(LINE[1])
        start += 1
    return dict        
    

f = open("constants.txt","r")
print get_fundamental_constants(f)
# {"Boltzmann constant": 1.380658e-23, "speed of light": 299792458.0,
#"proton mass": 1.6726231e-27,"gravitational constant": 6.67259e-11,
#"Avogadro number": 6.0221367e+23,"elementary charge": 1.60217733e-19,
#"Planck constant": 6.6260755e-34,"electron mass": 9.1093897e-31}