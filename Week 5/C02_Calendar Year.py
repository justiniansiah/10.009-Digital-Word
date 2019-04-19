month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} #dict
TESTTEST=0

def leap_year(year): #Returns True if provided year is a leap year, otherwise returns False.
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)
    if year % 4 > 0:
        return False
    elif year % 100 > 0:
        return True
    elif year % 400 > 0:
        return False
    else:
        return True

def day_of_week_jan1(year):
    if year < 1800 or year > 2099:
        return 0
    else:
        A = 5*((year-1)%4)
        B = 4*((year-1)%100)
        C = 6*((year-1)%400)
        D = ((1+A+B+C)%7)
    return D

def num_days_in_month(month_num,leap_year):

    if leap_year == True and month_num == 2:
        return 29
    else:
        return month_days[month_num]
    return
    

def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    month_name = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    
    out = []
    out.append(month_name[month_num])
    week = ""
    blank = " "
    spacer = " "
    counter = 1
    for i in range(first_day_of_month):
       week = week + blank + (spacer*2)
    
    for i in range(7-first_day_of_month):
        week += spacer*2
        week += str(counter)
        counter +=1
        
           
    out.append(week)
    
    while num_days_in_month+1>counter:
        week =""
        daytracker = 0
        while daytracker < 7:
            if counter < 10:
                week += spacer*2
                week += str(counter)
                counter += 1
                
            elif num_days_in_month+1>counter:
                global TESTTEST
                week += spacer
                week += str(counter)
                counter += 1
                first_day_of_month = (daytracker + 1)%7  #for next month's first day
                TESTTEST = first_day_of_month
            daytracker += 1
        out.append(week) 
    return out
#print construct_cal_month(2,3,28)  #test construct_cal_month  
    

def construct_cal_year(year):
    out=[]
    out.append(year)
    leap = leap_year(year) #leap
    first_day_of_month = day_of_week_jan1(year)
    for i in range (12):
        month_num = i+1
        DAYS = num_days_in_month(month_num,leap)
        current_month = construct_cal_month(month_num, first_day_of_month, DAYS)
        out.append(current_month)
        first_day_of_month = TESTTEST
        
    return out
    
#print construct_cal_year(2015)


def display_calendar(calendar_year):
    dater = "  S  M  T  W  T  F  S"
    YEAR = construct_cal_year(calendar_year)
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
    
def print_space_display_calendar (calendar):
    temp = calendar . replace (' ','*')
    return temp . replace ('\n','+\n')


ans= display_calendar (2015)
print print_space_display_calendar (ans)
#print display_calendar(2015)


