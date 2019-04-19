def getMRT(f):
    MRT = {}
    for i in f:
        line = i.strip()
        LINE = line.split(',')
        list = []
        for j in range(1,len(LINE)):
            list.append(LINE[j])
        MRT[LINE[0]]=list
    return MRT
    
def distance(d,s):
    ans = 0
    stations = s.split(",")
    
    if len(s) == 0: #check length of s
        ans = -2
    elif len(stations) ==1:
        ans = -1
    else:
        line1 = "a"
        line2 = "b"
        for i in d: #checking the lines of the 2 stations
            if stations[0] in d[i]:
                line1 = i
            if stations[1] in d[i]:
                line2 = i
        
        if line1 == line2: #same line
            railline = d[line1]
            for i in range(len(railline)):
                if stations[0] == railline[i]:
                    dist1 = i
                if stations[1] == railline[i]:
                    dist2 = i
            
            return abs(dist1-dist2)
        else:
            ans = -1
        
    return ans
    
# f= open ("mrt.txt", "r")
# d= getMRT (f)   

#s = "Convention Center,Millennia" #1
#s = "Pasir Ris,Bedok" #4
#s = "Downtown,Pasir Ris" #-1
#s = "Bedok" #-1
#s = "" #-2




print distance(d,s)
    
def test ():
    f= open ("mrt.txt", "r")
    d= getMRT (f)
    done = False
    while not done :
        s= raw_input ("Two stations please :")
        dist = distance (d,s)
        if dist != -2:
            print dist
        else :
            done = True
    print "Bye!"
    f. close ()
    
test()
    