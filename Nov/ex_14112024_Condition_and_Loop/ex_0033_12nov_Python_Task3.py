#Problem to find the max between two ( 3,4) → 4

Num1 = float (input("Enter the number1"))
Num2 = float (input("Enter the number2"))
Max_Number=max(Num1,Num2)
print(Max_Number)

#if else condition

if Num1>Num2:
    print ("Number1 is max")
else:
    print("Number 2 is max")

#edge case
#Num1=Num2 ->equal handled condition above
#String ->ABC - >ten->try and except - we will learn this in future
# -ve value - we will learn this in future