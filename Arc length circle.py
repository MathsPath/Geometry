import math

angle = float(input("Input an angle measure: "))

radius = float(input("Input radius of a circle: "))

circumference = 2 * math.pi * radius

ratio = angle / 360

print(f"Circumference = {2 * radius}π, Ratio = {angle}/360, Arc length ≈ {ratio * circumference}")