fruits = ("apple", "banana", "cherry", "orange", "kiwi")

# access by index
print(fruits[0])    # apple
print(fruits[2])   # cherry

# negative indexing
print(fruits[-1])   # kiwi
print(fruits[-2])   # orange

# range of indexes like slicing
print(fruits[1:4])  # ('banana', 'cherry', 'orange')

print(fruits[:3])   # from the start
print(fruits[2:])   # to the end

# check if item exists
if "apple" in fruits:
    print("apple is in the tuple")