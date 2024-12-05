from functools import wraps


def add_extra_scurity(fun):
    def wrapper():
        print("1. Before the function called")
        print("2. Add helmet,dashcam,gloves,keengaurd")
        fun()
        print("3.After function called")
        print("4.secure driving leave all the items")
    return wrapper()
@add_extra_scurity
def drive_ola_scooty():
    print("ola")

@add_extra_scurity
def driving_scooty():
    print("normal function")
    print("i am driving my scooty")
