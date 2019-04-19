def bmi(weight,height):
    w = weight * 0.45359237
    h = height * 0.0254
    bmi = w/(h**2)
    return bmi
    
print bmi(100,50)