def minutes_to_years_days(minutes):
    y = 365*24*60
    z = minutes%y
    days = z/(60*24)
    years = minutes/y    
    
    return years,days

print minutes_to_years_days(2000000000)
    