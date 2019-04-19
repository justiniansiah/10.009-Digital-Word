#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.
from copy import deepcopy

def get_nodes(fid):
    list = []
    for i in fid:
        j = i.strip()
        x=j.split()
        tup = (int(x[0]),int(x[1]))
        list.append(tup)
    return list

def create_graph(nodes):
    dict = {}
    for i in range(len(nodes)):
            if nodes[i][0] not in dict.keys():
                dict[nodes[i][0]] = {}
                dict[nodes[i][0]][nodes[i][1]]=1
            elif nodes[i][1] not in dict[nodes[i][0]]:
                dict[nodes[i][0]][nodes[i][1]]=1
            else:   
                dict[nodes[i][0]][nodes[i][1]]+=1
    
    for i in range(len(nodes)):
            if nodes[i][1] not in dict.keys():
                dict[nodes[i][1]] = {}
                dict[nodes[i][1]][nodes[i][0]]=1
            elif nodes[i][0] not in dict[nodes[i][1]]:
                dict[nodes[i][1]][nodes[i][0]]=1
            else:   
                dict[nodes[i][1]][nodes[i][0]]+=1            
                            
    return dict                
            

def get_friends(G,node):
    return G[node].keys()
    

def suggested_new_friends(G,node):
    friends = get_friends(G,node)

    dict = {}
    list = []
    list2= []
    for i in G:
        if i==node or i in friends:
            pass
        else:
            list.append(i)
            
    for i in G:
        count =0
        if i in list:
            for j in G[i].keys():
                if j in friends:
                    count+=1
            
            list2.append(count)
    
    for i in range(len(list)):
        dict[list[i]]=list2[i]
        
    max = 0
    key = []
    for i in dict:
        if dict[i] >= max:
            max = dict[i]
            key.append(i)
            
            
    return (key,max)            
    
    
f = open("facebook_less.txt","r")
#f = open("sutdbook1.txt","r")
#f = open("sutdbook2.txt","r")

nodes = get_nodes(f)
G = create_graph(nodes)
print get_friends(G,0)
# print suggested_new_friends(G,0)


f.close
