def fahrenheit_to_celsius(temp):
    temp -= 32
    temp *= 5.0
    temp /= 9.0
    return temp

print fahrenheit_to_celsius(212)