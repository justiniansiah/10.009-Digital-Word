# ##### PART B #####

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
    out.append(cel)
    
    temp = []
    for i in range(11):
        temp.append(round(f_to_c(cel[i]),1))
    out.append(temp)
    
    temp = []
    for i in range(11):
        temp.append(round(f_to_c_approx(cel[i]),1))  
    out.append(temp)
    
    return out
    
print get_conversion_table()
