# inheritance allows us to define a class 
# that inherits all the methods and properties from another class

# parent class is the class being inherited from, also called base class
# child class is the class that inherits from another class, also called derived class



# create a parent class
# any class can be a parent class, so the syntax is the same as creating any other class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# use the Person class to create an object 
# and then execute the printname method
x = Person("John", "Doe")
x.printname()



# create a child class
# to create a class that inherits the functionality from another class
# send the parent class as a parameter when creating the child class

class Student(Person):
    pass
# use pass when you do not want to add any other properties or methods to the class

# now the Student class has the same properties and methods as the Person class
# use the Student class to create an object, and then execute the printname method
x = Student("Mike", "Olsen")
x.printname()


# adding the __init__() function
# it is called automatically every time the class is being used to create a new object
# when you add the __init__() function, the child class 
# will no longer inherit the parent's __init_() function 

# BUT the child's __init__() function overrides the inheritance of the parent's __init__() function
# so to keep the inheritance of the parent's __init__() function,
# add a call to parent's __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# now we have sucessfully added the __init__() function, 
# and kept the inheritance of the parent class, 
# and we ready to add functionality in the __init__() function