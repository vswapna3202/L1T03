# This program inputs the sides of a triangle and calculates its area and prints it. It uses
# Math functions
# import math library
import math

# Input the 3 sides of the triangle and assign it to variables side1, side2 and side3 respectively
side1 = int(input("Enter side1 of the triangle: "))
side2 = int(input("Enter side2 of the triangle: "))
side3 = int(input("Enter side3 of the triangle: "))

# Calculate the value s which is perimeter of triangle divided by 2
s = (side1 + side2 + side3) / 2

# Calculate the area of the triangle using the sqrt function from math library on product of s,
# (s - side1), (s - side2) and (s- side3)
area = math.sqrt(s*(s - side1) * (s - side2) * (s - side3))

# Print the calculated area to the console
print(f"Area of the triangle is: {area}")