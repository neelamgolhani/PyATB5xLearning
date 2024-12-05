#user define function type
#**User Defined**

#1. `The can't return -> non return`
#2. They can return something
#3. They have parameters
#4. `They don't parameters / arguments`

#1. `The can't return -> non return`
#no parameter, no return type / no argument
def greet():
    print("Hello")
greet()


#2. No return type with arguments

def greet_by_name(name):
    print("hello",name)
greet_by_name("Neelam")

#3. No return type but with default arguments (positinal Arguement)

def greet_by_name2(name="golhani"):
    print("hello",name.upper())
greet_by_name2("Devanshi")
greet_by_name2()

def multiple_arg(name1="a",name2="b"):
    print("multiple argument - >",name1,name2)
multiple_arg()
multiple_arg(name1="Neel")
multiple_arg(name2="Neel")
multiple_arg(name1="Neel",name2="gol")
multiple_arg("NEEL")

#4. Argument and return type
def sum_of_two_num(a,b):
    return a+b
result=sum_of_two_num(4,5)
print(result)

def sum_of_two_num_with_default_value(num1=100,num2=200):
    print("i will sum the 2 number")
    return num1+num2
result=sum_of_two_num_with_default_value(num1=34,num2=34)
print(result)
result=sum_of_two_num_with_default_value()
print(result)



