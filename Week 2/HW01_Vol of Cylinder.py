from math import pi
def vol_cylinder(radius,length):
    area = radius * radius * pi
    vol = area * length
    return area,vol

print vol_cylinder (2.2 ,5.0)