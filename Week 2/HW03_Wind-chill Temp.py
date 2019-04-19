def wind_chill_temp(ta, v):
   wc = 35.74 + (0.6215*ta) - (35.75*(v**0.16)) + (0.4275)*(ta)*(v**0.16)
   return wc
   
print wind_chill_temp (2.2,4)
