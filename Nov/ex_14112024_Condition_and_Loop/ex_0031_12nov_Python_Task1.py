#Write a program to take a user age and let him know if he can go the club.  21
#Logic building formula
#Step 1 -> User i/P ->Data type ->int
#o/p - Data type - String

#Step 2 - Rough logic
#age>21 - Can go
#age<21 - Can not go

#step 3 - Write the logic

User_age = int(input("Enter User age"))
if User_age >=21:
    print("User can enter to the club")
else:
    print("User is not allowed to get in to the club")

#tarnary method
print("User can enter to the club" if int(input("Enter User age"))>=21 else "User is not allowed to get in to the club")

#Check for the edge CASE
#-ve value for age
# Extremely high value for age
#Alpha numeric value
#

#Step 5:- Optimization the code.
#handle all edge case