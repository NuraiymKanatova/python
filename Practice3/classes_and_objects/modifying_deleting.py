# modifying object properties
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("Toyota", 2012)

c.year = 2015                  # changed the property
c.color = "black"              # added new property

print(c.brand, c.year, c.color)



# deleting object properties
class User:
    def __init__(self, login):
        self.login = login
        self.role = "student"

u = User("Anna")

del u.role                    # deleted role

print(u.login)
# print(u.role) will give an error

class Box:
    pass

b = Box()
b.value = 10

del b
# print(b) does not exist