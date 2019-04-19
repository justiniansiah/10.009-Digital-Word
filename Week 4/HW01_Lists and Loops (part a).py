# ##### PART A #####

def f_to_c (temp):
    temp -= 32
    temp *= 5.0
    temp /= 9.0
    return temp

def f_to_c_approx(temp):
    temp = (temp - 30)/2
    return temp
    
def get_conversion_table():
    cel = []
    out = []
    for i in range (0,101,10):
        cel.append(i)
    
    for i in range(10):
        temp = []
        temp.append(cel[i])
        temp.append(round(f_to_c(i),1))
        temp.append(round(f_to_c_approx(i),1))
        out.append(temp)
    
    return out
    
print get_conversion_table()
