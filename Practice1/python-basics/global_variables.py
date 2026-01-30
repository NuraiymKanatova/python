# global variable
x = "Python"

def my_function():
    print(x)

my_function()


def change_value():
    global x
    x = "Programming"

change_value()
print(x)
