# random module used to generate random numbers or randomly select elements
# import
import random
# it generates pseudorandom values using an algorithm


# random.random()
# returns a float between 0.0 and 1.0 (not including 1)
import random
x = random.random()
print(x)
# example output: 0.3748291


# random.randint(a,b)
# returns an integer between a and b inclusive
import random
x = random.randint(1, 10)
print(x)
# includes both 1 and 10


# random.choice(sequence)
# returns one random element from a list (or tuple, string)
import random
names = ["Ivan", "Anna", "Max"]
selected = random.choice(names)
print(selected)
# returns one random item
# sequence can not be empty


# random.shuffle(list)
# shuffles a list in place
import random
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)
# it modifies the original list
# it returns None