#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def num_of_sol(n):
    count = 0
    for j in range(n+1):
        count += sum([sum(range(i)) for i in range(j+3)])
    return count

print num_of_sol(3)
print num_of_sol(4)
print num_of_sol(120)
  
    

