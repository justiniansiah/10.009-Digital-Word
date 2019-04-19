def get_even_list(list):
    newlist = []
    for i in range (len(list)):
        if list[i]%2 == 0:
            newlist.append(list[i])
    return newlist

print get_even_list([1,2,3,4,5])
print get_even_list([11,22,33,44,55])
print get_even_list([10,20,30,40,50])
print get_even_list([11,21,31,41,51])