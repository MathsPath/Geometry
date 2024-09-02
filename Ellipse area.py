import math

semi_major = float(input("Input semi-major axis of an ellipse: "))
semi_minor = float(input("Input semi-minor axis of an ellipse: "))

print(f"{semi_major * semi_minor}π ≈ {math.pi * semi_major * semi_minor}")