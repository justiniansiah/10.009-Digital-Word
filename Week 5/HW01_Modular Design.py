def get_data():
    a = raw_input("Enter integer pair (hit Enter to quit):")
    return
    
def extract_values(values):
    list = values.split()               #splits a string into list
    return (int(list[0]),int(list[1]))  #returns tuple value


def calc_ratios(values):
    if values[1] == 0:
        return None
    else:
        return float(values[0])/values[1]
    return
    
#get_data()
print extract_values("134 289")
print calc_ratios((134, 289))


