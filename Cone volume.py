import math

height = float(input("Height: "))
radius = float(input("Radius of a base: "))

print(f"Volume: {(1 / 3) * radius**2 * height}π ≈ {(1 / 3) * math.pi * radius**2 * height}")