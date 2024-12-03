#Match statement = Switch in java
#match the output
#python >3.10

#syntax
#match Variable_name:
#   case pattern1:
#       Code block
#   case pattern2:
#       Code block

#write a program to ask the user which browser he wants to run automation.
#logic building
#i/p Browser_name (string) = O/p (string)

browser_name = input("Enter browser name \n")
match browser_name:
    case "firefox":
        print("Starting Firefox")
    case "chrome":
        print("Launch chrome")
    case "edge":
        print("Start edge")
    case "safari":
        print("Launch safari")
    case _:
        print("No browser found")
