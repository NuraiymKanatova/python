# the generator has a following syntax:
def fun():
    yield 1
    yield 2
    yield 3

for val in fun():
    print(val)

# output: 
# 1 
# 2 
# 3

# yield - is used in generator functions to provide a sequence of values over time
# when yield is executed, it pauses the function, returns the current value and retains the state of the functions
# this allows the function to continue from same point when called again

# return - is used to exit a function and return a final value
# once return is executed, function is terminated immediately and no state is retained
# this is suitable for cases where a single result is needed from a function

def fun():
    return 1 + 2 + 3

res = fun()
print(res)
# output: 6