# arbitary arguments - *args

# if you do not know how many arguments will be passed into your function
# add a * before the parameter name

# this way function will receive a tuple of arguments

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# accessing individual arguments from *args
def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

# using *args with regular arguments
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")