# a classes have a built-in called __init__()
# which is always executed when the class is being initiated

# the __init__() method is used to assign values to object properties
# or to perform operations that are neccessary when the object is being created


# create a class named Person, use the __init__() method to assign for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# the __init__() method is called automatically every time the class is being used to create a new object

# without the __init__() method, 
# you would need to set properties manually for each object
# create a class without __init__()
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# using __init__() makes it easier to create objects with initial values
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

# default values in __init__()
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# multiple parameters
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)