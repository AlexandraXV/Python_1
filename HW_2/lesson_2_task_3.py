import math

def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

side = 2.5
square_area = square(side)

print(f"Площадь квадрата со стороной {side}: {square_area}")