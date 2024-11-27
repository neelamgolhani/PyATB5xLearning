#Write a program to take a user age and let him know if he can go the club.  21

User_age = int(input("Enter User age"))
if User_age >=21:
    print("User can enter to the club")
else:
    print("User is not allowed to get in to the club")

print("User can enter to the club" if int(input("Enter User age"))>=21 else "User is not allowed to get in to the club")