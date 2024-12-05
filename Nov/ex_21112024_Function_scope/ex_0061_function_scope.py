pb_global_b=12 #//global variable

def my_function():
    pa_local=10 #// local variable
    print(pa_local)
    print(pb_global_b)
#print(pa_local) // calling local variable outside the function is not allowed
my_function()