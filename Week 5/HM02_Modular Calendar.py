import Calendar as Cal

def display_calendar_full(calendar_year):
    dater = "  S  M  T  W  T  F  S"
    YEAR = Cal.construct_cal_year(calendar_year)
    i = 1
    out = ""
    while i < 13:
        for j in range(len(YEAR[i])): 
            if j == 1:
                out += dater + "\n"
                
            out += YEAR[i][j] + "\n"
        
        if i <12: #only print new line from Jan to Nov
            out += "\n"
        i+=1
    
    return out[:-1] #removes extra spacing

def display_calendar(calendar_year, month):
    if month == None:
        return display_calendar_full(calendar_year)
    else:
        dater = "  S  M  T  W  T  F  S"
        YEAR = Cal.construct_cal_year(calendar_year)
        out = ""
        for j in range(len(YEAR[month])): 
            if j == 1:
                out += dater + "\n"
                
            out += YEAR[month][j] + "\n"
        return out[:-1] #removes extra space
        
    return
    
print display_calendar(2015,8)



