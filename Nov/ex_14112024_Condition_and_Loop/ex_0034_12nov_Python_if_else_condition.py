#Write a program to find the max among 3 numbers.
#logic building
#Step 1 -> User i/P Num1, Num2, Num3 ->Data type ->int
#o/p - Data type - String or int

#Step 2 - Rough logic
#if Else - 1 condition

#Syntax
#if Condition 1:
#    print("do 1")
#if condition 2:
 #   print("do 2")
#if condition 3:
#    print("do 3")
#else:
#    print("do for else")



#step 3 - Write the logic

Num1 = int(input("Enter Number1"))
Num2 = int(input("Enter Number2"))
Num3 = int(input("Enter Number3"))
if Num1 >=Num2 and Num1>=Num3:
    print("Max Number is Num1")
if Num2 >=Num1 and Num2>=Num3:
    print("Max Number is Num2")
else:
    print("Max Number is Num3")

#tarnary method
print("User can enter to the club" if int(input("Enter User age"))>=21 else "User is not allowed to get in to the club")

#Check for the edge CASE
#-ve value for age
# Extremely high value for age
#Alpha numeric value
#

#Step 5:- Optimization the code.
#handle all edge case