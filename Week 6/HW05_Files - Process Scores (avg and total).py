#unspecified number of score in file
#read and return total and average

def process_scores(f):
    score = []
    for i in f:
        line = i.strip()
        store = line.split()
        storer = store[0]
        score.append(float(storer))
    total = sum(score)
    average = total/len(score)
    return total,average
    
f= open ("scores.txt","r")
print process_scores(f)
    
