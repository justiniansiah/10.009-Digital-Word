from CheckoffQ5 import compound_value_sixth_months

amt=float(raw_input("Enter the Initial Amount: "))

rate=float(raw_input("Enter the Rate: "))

final = compound_value_sixth_months(amt,rate)

print "With initial $ %d at interest rate of %.2f" %(amt,rate)
print "After 6 months, final amount is $ %f" %(final)