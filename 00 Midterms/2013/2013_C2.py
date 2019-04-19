def seriesSummer(firstTerm,r,epsilon,termMax):
    CHECK = True
    counter = 0
    TERMS = []
    nextTerm = firstTerm
    nextnextTerm = nextTerm*r
    while CHECK:
        if(abs(nextnextTerm - nextTerm) < epsilon):# or (len(TERMS)>=termMax):
            TERMS.append(nextTerm)    
            nextTerm *= r 
            nextnextTerm = nextTerm*r
            SUM = sum(TERMS)
            nlist = []
            if len(TERMS)> 3:
                no = 3
            else:
                no = len(TERMS)
            #counter = 3
            for i in range(no):
                nlist.append(TERMS[-3+i])
            CHECK = False
            
        elif(len(TERMS)>=termMax):
            SUM = sum(TERMS)
            nlist = []
            if len(TERMS)> 3:
                no = 3
            else:
                no = len(TERMS)
            for i in range(no):
                nlist.append(TERMS[-no+i])
            CHECK = False
        else:
            TERMS.append(nextTerm)    
            nextTerm *= r 
            nextnextTerm = nextTerm*r  
        
    return SUM,len(TERMS),nlist
    
print seriesSummer(1,2/3.0,0.003,30)
#print seriesSummer(1,2/3.0,0.1,2)
#print seriesSummer(7/10.0,1/10.0,0.001,30)