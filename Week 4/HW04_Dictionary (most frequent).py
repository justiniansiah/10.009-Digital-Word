def most_frequent(list):
    dict = {}
    for i in list: #making the dictionary
        count = list.count(i)
        if i not in dict.keys():
            dict[i] = count
            
    max_count = 0 
    for i in dict: #finding the modal number
        if dict[i] >= max_count:
            max_count = dict[i]
            
    modeset = []
    for i in dict: #making the set of numbers with the mode
        if dict[i] == max_count:
            modeset.append(i)
    
    return modeset
    
print most_frequent([2,3,40,3,5,4,-3,3,3,2,0]) #[3]
print most_frequent([9,30,3,9,3,2,4]) #[9, 3]