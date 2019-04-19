from CheckoffQ3 import minutes_to_years_days

minutes=raw_input("Enter the number of minutes: ")
#print minutes, type(minutes)
minutes=int(minutes)
#print minutes, types(minutes)
years, days = minutes_to_years_days(minutes)
#print years, days
print minutes, "minutes is approximately", \
    years, "years and", days, "days"
print "%d minutes is approximately %d years and %d days." %(minutes,years,days)