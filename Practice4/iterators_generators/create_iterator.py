# to create an object/class as an iterator you have to 
# implement the methods __iter__() and __next__() to your object

# the __iter__() method acts similar as __init__(), 
# you can do operations (initializing, etc.) 
# but must always return the iterator object itself

# the __next__() method also allows you to do operations, 
# and must return the next item in the sequence

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# output will be 
# 1 
# 2 
# 3 
# 4 
# 5