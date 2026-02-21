# we can also use a for loop to iterate through an iterable object

# iterate the values of a tuple
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# iterate the characters of a string
mystr = "banana"

for x in mystr:
    print(x)

# the for loop actually creates an iterator object 
# and executes the next() method for each loop