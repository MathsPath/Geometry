import math

angle = float(input("Input an angle measure: "))

radius = float(input("Input radius of a circle: "))

area = math.pi * radius**2

ratio = angle / 360

print(f"Area = {radius**2}π, Ratio = {angle}/360, Sector area ≈ {ratio * area}")