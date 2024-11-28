#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is
# equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or
# scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

#logic Building

#Step 1 ->
#            I/P - int Side1, Side2, Side3
#            o/p - String

#Step 2-> Rough logic

side1 = int(input("enter the side1 \n"))
side2 = int(input("enter the side2 \n"))
side3 = int(input("enter the side3 \n"))

if (side1==side2) and (side1==side3) :
    print ("the triangle is equilateral (all sides are equal)")
elif (side1==side2) and (side1!=side3) :
    print("isosceles (exactly two sides are equal)")
else:
    print("scalene (no sides are equal)")



