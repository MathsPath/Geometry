# c - hypotenuse, only right triangles! a,b - legs
# leave '' for side we look for
import math

a = input("Input a value for A side: ")
b = input("Input a value for B side: ")
c = input("Input a value for C side: ")

if c == '':
    c = math.sqrt( float(a) ** 2 + float(b) ** 2 )
    print(c)
if a == '':
    a = math.sqrt( float(c)**2 - float(b)**2 )
    print(a)
if b == '':
    b = math.sqrt( float(c)**2 - float(a) ** 2 )
    print(b)

