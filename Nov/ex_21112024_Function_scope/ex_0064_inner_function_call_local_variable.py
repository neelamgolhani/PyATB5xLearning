def outer_function():
    local_var="a"
    def inner_function():
        print(local_var)
    def inner_function2():
        print(local_var)
    inner_function()
    inner_function2()
outer_function()

