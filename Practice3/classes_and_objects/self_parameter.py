# the self parameter is a reference to the current instance of the class
# it is used to access properties and methods that belong to the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()
# the self parameter must be the first parameter of any method in the class

# without self, python would not know which object's properties you want to access:
class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

# self does not have to be named as "self"
class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

# while you can use a different name, it is strongly recommended to use self itself

# accessing properties with self
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# you can call one method from another method using self
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello," + self.name
    
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()