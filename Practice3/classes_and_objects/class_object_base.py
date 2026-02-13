# almost everything in python is an object, with its properties and methods
# a class is like an object constructor, or a "blueprint" for creating objects

# create a class
class MyClass:
    x = 5


# create an object
p1 = MyClass()
print(p1.x)


# delete objects
del p1


# multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# each object is independent and has its own copy of the class properties