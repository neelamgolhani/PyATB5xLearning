#Ternay Operator with user input
# If your is age>18 then allow to vote else not allowed


age = int(input("Enter your age"))
if age>18:
    print("please vote")
else:
    print("not allowed")

#using ternary operator
print("allow to vote" if age>18 else print("Not allowed"))
print ("allow to vote" if int(input("Enter your age"))>18 else print("Not allowed"))

