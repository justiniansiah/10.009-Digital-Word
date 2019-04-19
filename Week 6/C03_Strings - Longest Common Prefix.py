def longest_common_prefix(s1,s2):
    out = ""
    # if len(s1)<=len(s2):
    #     for i in range(len(s1)):
    #         if s1[i] == s2[i]:
    #             out+=s1[i]
    #         else:
    #             return out
    #                 
    # else:
    #     for i in range(len(s2)):
    #         if s1[i] == s2[i]:
    #             out+=s1[i]
    #         else:
    #             return out
    
    minimum = min(len(s1),len(s2))
    for i in range(minimum):
        if s1[i] == s2[i]:
            out+=s1[i]
        else:
            return out
    
    return out

print longest_common_prefix("distance", "disinfection") #dis
print longest_common_prefix("testing", "technical") #te
print longest_common_prefix("drinking", "drinker") #drink
print longest_common_prefix("rosses", "crosses") #
print longest_common_prefix("distancetion", "distance") #distance



    
