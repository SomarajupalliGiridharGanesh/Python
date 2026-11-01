#Area of the Square

side   = float(input("Enter the side of an square : "))
peris  = side*4
area_s = side*side
print(f"The perimeter of the square = {peris}")
print(f"    The area of the square  = {area_s}")

#area of the Triangle using heron's formula
import math  
a = float(input("Enter the first side of triangle  = "))
b = float(input("Enter the second side of triangle = "))
c = float(input("Enter the third side of triangle  = "))
s = (a+b+c)/2
peri_t = a+b+c
area_t = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"The perimeter of triangle = {peri_t}  ")
print(f"The area of the triangle  = {area_t} ")

#area of circle
import math
r = float(input("Enter the radius of the circle = "))
print("perimeter of the circle = " ,2*math.pi*r)
print("the Area of the circle  = " ,math.pi*r*r)

