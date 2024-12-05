#write a program , take a user name and say hello to him

user_name = input("enter user name")
def Say_hello_to_user(user_name):
    print("Hello",user_name)
Say_hello_to_user(user_name)

#user input can be written after defining the function


def Say_hello_to_user(user_name):
    print("Hello",user_name)
user_name = input("enter user name")
Say_hello_to_user(user_name)