#Checking for a Leap Year , 2024 → Yes
#Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

#logic Building

#Step 1 ->
#            I/P - int year
#            o/p - String

#Step 2-> Rough logic

year = int(input("enter the year \n"))
reminder=year%4
if reminder==0:
    print ("Then leap year")
else:
    print("Non leap year")



