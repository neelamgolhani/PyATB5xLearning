#WAP to calculate the area of a circle given its radius the formula
# Area = π × r 2. Where: π = the number pi (3.1416...)

#logic building formula
#step 1 figure out the input and output
#input Radius -> Datatype ->float
#pi=3.14
#Power ->pow or ** ->any
#o/p -> Float
#Print

Radius = float(input("Enter the radius"))
Area = 3.14*Radius**2
print("circle ->", Area)
print(f"Area of circle-> {Area:.2f}") # {Area:.2f after dot it gives decimal number}

import math
print (math.pi)
print(math.pow (Radius,2))
area= math.pi * math.pow (Radius,2)

print("Area of circle->", 3.14*float(input("Enter the radius"))**2)
