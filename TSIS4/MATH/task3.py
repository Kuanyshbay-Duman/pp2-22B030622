import math


def area_of_polygon(n, s):
    area = (1/4) * n * s**2 * (1/math.tan(math.pi/n))
    return round(area)


number_of_sides = int(input("Enter a number of side: "))
length_of_side = int(input("Enter length of side: "))

print(area_of_polygon(number_of_sides, length_of_side))
