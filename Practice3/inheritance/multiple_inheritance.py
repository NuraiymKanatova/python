# basic multiple inheritance
# a class can inherit from more than one parent

class A:
    x = 10
    
class B:
    y = 20
    
class C(A, B): # inherits attributes both from A and B
    pass

obj = C()
print(obj.x)  # from A
print(obj.y)  # from B

# with __init__()

class A:
    def __init__(self):
        self.a = "Hello"
    
class B:
    def __init__(self):
        self.b = "World"

class C(A, B):   
    pass         

obj = C()        

# this will not work properly, because python only calls parent's __init__ automatically
# C inherits from (A, B) so only A.__init__() runs
# obj.b will not exist


# order matters
class A:
    value = "From A"

class B:
    value = "From B"

class C(A, B):
    pass

print(C.value)  # From A

# python searches parents from left to right
# so if you will change the order

class C(B, A):
    pass

print(C.value)  # From B