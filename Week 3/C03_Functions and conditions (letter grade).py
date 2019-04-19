def letter_grade(mark):
    if mark > 100:
        return "None"
    elif mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 0:
        return "E"
    else:
        return "None"
        
print letter_grade (102)
print letter_grade (100)
print letter_grade (83)
print letter_grade (75)
print letter_grade (67)
print letter_grade (52)
print letter_grade (-2)
