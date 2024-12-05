#WAP sum of 3 numbers using user input.
#if user does not enter any number ,use default (100,200,300)

num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

def three_num_sum(n1=100,n2=200,n3=300):
    return n1+n2+n3
result=three_num_sum(num1,num2,num3)
print("Sum of 3 num ->" ,result)

result2=three_num_sum()
print("Sum of 3 num is ->" ,result2)
result2=three_num_sum(10)
print("Sum of 3 num is ->" ,result2)
result2=three_num_sum(10,20)
print("Sum of 3 num is ->" ,result2)
result2=three_num_sum(10,20,30)
print("Sum of 3 num is ->" ,result2)