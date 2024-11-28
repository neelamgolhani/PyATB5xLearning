#Write a program that calculates and displays the letter grade for a
# given numerical score (e.g., A, B, C, D, or F) based on the
# following grading scale:
from tokenize import String

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

#logic Building

#Step 1 ->
#            I/P - int
#            o/p - String

#Step 2-> Rough logic

Score = int(input("enter the score \n"))

if Score>=90 and Score<=100:
    print ("Grade A+")
elif Score>=80 and Score<=89:
    print("Grade A")
elif Score>=70 and Score<=79:
    print("Grade B")
elif Score>=60 and Score<=69:
    print("Grade C")
else:
    print("Fail")


