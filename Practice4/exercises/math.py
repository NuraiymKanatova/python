# Write a Python program to convert degree to radian.
# Input degree: 15
# Output radian: 0.261904
import math

degree = float(input())
radian = degree * math.pi / 180

print(round(radian, 6))



# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5
height = float(input())
base1 = float(input())
base2 = float(input())

area = ((base1 + base2) / 2) * height

print(area)



# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
import math

n = int(input())
s = float(input())

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(area)



# Write a Python program to calculate the area of a parallelogram.
# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0
base = float(input())
height = float(input())

area = base * height

print(area)