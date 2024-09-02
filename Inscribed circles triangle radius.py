import math

a = float(input("Input length for side A: "))
b = float(input("Input length for side B: "))
c = float(input("Input length for side C: "))

perimeter = a + b + c
semi_perimeter = perimeter / 2

area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

print(f"Radius = {area / semi_perimeter}")

