def position_velocity(vinit, t):
    y1 = (vinit*t) - (1.0/2)*(9.81)*(t**2)
    y2 = vinit - (9.81*t)
    y1 = round (y1,2)
    y2 = round (y2,2)
    return y1,y2
    
print position_velocity (0.0,5.0)