#### This problem will be graded manually.
#### Please ignore the points given out by Tutor.

def get_students(students, course):
    Sub = {}
    for i in range(len(students)):
        for j in students[i][1]:
            if j not in Sub.keys():
                Sub[j] = []
                Sub[j].append(students[i][0])
            else:
                Sub[j].append(students[i][0])
    if course in Sub.keys():
        ans = Sub[course]
    else:
        ans = []
    
    return ans
        
print get_students(students,"Philosophy")
print get_students(students,"History")
print get_students(students,"Math")
print get_students(students,"CompSci")




#As stated in question, use the following list to test your solution. 
students=[("Alan",["CompSci", "Physics", "Math"]),
              ("Justin",["Math","CompSci","Stats"]),
              ("Edward",["CompSci","Philosophy", "Economics"]),
              ("Margaret",["InfSys","Accounting","Economics","CommLaw"]),
              ("Philip",["Sociology","Economics", "Law", "Stats","Music"]),
              ("Mary",["Math","CompSci","Stats"]),
              ("Vera",["CompSci","Philosophy","Economics"]),
              ("Mike",["InfSys","Accounting","Economics","CommLaw"]),
              ("Donna",["Sociology","Economics","Law","Stats"])]
