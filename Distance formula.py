# 2 points, find distance coordinate plane
import math

a = input("Input A coordinate (separate with ','): ").split(',')
b = input("Input B coordinate (separate with ','): ").split(',')

def distance(point1, point2):
    return math.sqrt(((float(point1[0]) - float(point2[0]))**2) + ((float(point1[-1]) - float(point2[-1]))**2))


print(distance(a, b))