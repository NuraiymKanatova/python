# python also has super() function 
# that will make the child clas inherit all the methods and properties from its parent
class Person:
    pass
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# by using the super() function, you do not have to use the name of the parent element
# it will automatically inherit the methods and properties from its parent