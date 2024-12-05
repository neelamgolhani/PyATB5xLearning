#Checking for a Leap Year , 2024 → Yes
#Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
from operator import truediv

#the year is multiple of 400.
#The year is multiple of 4 and not a multiple of 100.

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

print("-----------------------------------------------")
#sir explained
def check_leap_year(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False

year = 2024

if check_leap_year(year):
    print(year,"->yes")
else:
    print(year,"->NO")




