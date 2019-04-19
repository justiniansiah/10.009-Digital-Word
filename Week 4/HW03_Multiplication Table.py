def multiplication_table(n):
    if n <= 0:
        return "None"
    else:
        row = []

        column = [[] for x in range(n)] 
        for i in range(n):
            row.append(i+1)
        for i in range(n):
            nrow =[]
            for j in row:
                nrow.append(j*(i+1))
            column[i]= nrow
    return column

print multiplication_table(7) #[[1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 8, 10, 12, 14], [3, 6, 9, 12, 15, 18, 21],[4, 8, 12, 16, 20, 24, 28], [5, 10, 15, 20, 25, 30, 35],[6, 12, 18, 24, 30, 36, 42], [7, 14, 21, 28, 35, 42, 49]]
print multiplication_table(1) #[1]
print multiplication_table(0) #None
print multiplication_table(2) #[[1, 2], [2, 4]]
print multiplication_table(-1) #None