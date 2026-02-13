# a lambda function is a small anonymous function
# a lambda functon can take any number of arguments
# but can only have one expression

# the result is excecuted and the result is returned as:
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# lambda function is best
# when you have an argument to be multiplied to an uknown number
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
mydoubler = myfunc(3)
print(mydoubler(11))