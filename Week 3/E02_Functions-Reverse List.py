def my_reverse(list):
    # return list[::-1]
    list2 = []
    for i in range (len(list)):
        list2.append(list[len(list)-i-1])
    return list2
    
print my_reverse([5,-2,15,4])