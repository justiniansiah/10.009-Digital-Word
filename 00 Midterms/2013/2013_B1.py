def getDict(f):
    out = {}
    for i in f:
        a=i.split()
        temp = [a[1],a[2],a[3]]
        out[a[0]]=temp
    return out
     
    
def searchDict(d):
    input = raw_input("Enter an event: ")
    if input in d:
        temp = d[input]
        out = ""
        for i in temp:
            out+=i
            out+= " "
        print out
        return searchDict(d)
    elif input == "*":
        print "Bye!"
        return
    else:
        print "No such event."
        return searchDict(d)
    return
    
    
def test():
    f = open('data.txt','r') 
    d = getDict(f)
    searchDict(d)
    return
    
test()
    