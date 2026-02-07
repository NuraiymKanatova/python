# you can send arguments with the key = value syntax.
# and even if we change the order of arguments, nothing will change

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
# output:   
# I have a dog 
# My dog's name is Buddy