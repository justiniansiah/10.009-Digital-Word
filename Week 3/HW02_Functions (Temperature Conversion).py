def temp_convert(type,no):
    if type == "C":
        return farenheit_to_celsius(no)
    elif type == "F":
        return celsius_to_farenheit(no)
    else:
        return "None"
    
def farenheit_to_celsius(F):
    C = (F-32)*float(5)/9
    return C

def celsius_to_farenheit(C):
    F = C*float(9)/5 + 32
    return F
    
print temp_convert("F",32)