import time
from functools import wraps


def time_decorator(fun):
    def wrapper():
        start_time=time.time()
        print(start_time)
        fun()
        end_time=time.time()
        print(end_time)
        print("totel time taken->" ,end_time-start_time)
    return wrapper()

def print_log(fun):
    def wrapper():
        print("starting_logs")
        fun()
        print("End_logs")
    return wrapper()

@print_log
@time_decorator
def test_ui_1():
    print("add function,time taken by this functionality 1")
    time.sleep(2)

test_ui_1()
@time_decorator
def test_ui_2():
    print("add function,time taken by this functionality 2")
    time.sleep(5)
test_ui_2()

