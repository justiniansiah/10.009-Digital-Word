def minmax_in_list(list):
    if len(list) == 0:
        return "(None, None)"
    else:
        Min = list[0]
        Max = list[0]
        for i in range(len(list)):
            if Max < list[i]:
                Max = list[i]
            if Min > list[i]:
                Min = list[i]
        # Min = min(list)
        # Max = max(list)
        return Min,Max
    
    
    
print ( "Test case 1: [1 ,2 ,3 ,4 ,5]" )
print minmax_in_list ([1 ,2 ,3 ,4 ,5])

print ( "Test case 2: [1 ,1 ,3 ,0]" )
print minmax_in_list ([1 ,1 ,3 ,0])

print ( "Test case 3: [3 ,2 ,1]" )
print minmax_in_list ([3 ,2 ,1])

print ( "Test case 4: [0 ,10]" )
print minmax_in_list ([0 ,10])

print ( "Test case 5: [1]" )
print minmax_in_list ([1])

print ( "Test case 6: []" )
print minmax_in_list ([])

print ( "Test case 7: [1 ,1 ,1 ,1 ,1]" )
print minmax_in_list ([1 ,1 ,1 ,1 ,1])




        