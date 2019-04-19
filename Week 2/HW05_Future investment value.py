def investment_val(amount, annualRate, years):
    ret = amount * ((1+((annualRate/12)/100))**(12*years))
    ret = round(ret,2)
    return ret

print investment_val (1000,2.25,0.5)