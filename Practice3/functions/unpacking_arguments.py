# the * and ** operators can also be used 
# when calling functions to unpack a list or dictionary
# into separate arguments

# unpacking lists with *
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # same as: my_fucntion(1, 2, 3)
print(result)

# unpacking dictionaries with **
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)
# same as: my_function(fname="Emil", lname="Refsnes")