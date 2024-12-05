from functools import wraps


def add_befor_UI_after_UI(fun):#// instead of fun we can give direct function name "test_ui()"
    def wrapper(): #// this Wrapper name can be anything but company standard and easy to learn
        print("1.Before running UI")
        print("2. start the browser")
        fun() #// test_ui()
        print("3.After running UI")
        print("4.quite the browser")
    return wrapper()

@add_befor_UI_after_UI
def test_ui():
    print(">>I will test the UI")

