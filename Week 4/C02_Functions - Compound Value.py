def compound_value_months (savings,interest,n):
    rate = interest/12.0
    x = 0
    out = 0
    for i in range (n):
        out = (savings+x)*(1+rate)
        x = out
    return round(out,2)
    
print compound_value_months(100,0.05,6) #608.81
print compound_value_months(100,0.03,7) #707.04
print compound_value_months(200,0.05,8) #1630.29
print compound_value_months(200,0.03,1) #200.5
print compound_value_months(200,0.05,0) #0.0