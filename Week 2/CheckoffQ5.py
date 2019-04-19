def comp (amt,org,sto,rate,y):
    if y==0:
        return amt
    else:
        amt = (amt+org)*(1+(rate/12))
        org = sto
        amt = comp(amt,org,sto,rate,y-1)
        return amt
def compound_value_sixth_months(amt, rate):
    rr = comp (amt,0.0,amt,rate,6)
    return rr
    