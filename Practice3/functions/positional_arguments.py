# if a function with arguments without using keywords
# they are called positional arguments
# the change in order wil change the meaning of a sentence

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
# output:   
# I have a dog 
# My dog's name is Buddy