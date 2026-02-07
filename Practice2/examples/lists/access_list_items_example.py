fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

# access by index
print(fruits[0]) # apple
print(fruits[2]) # cherry

# negative indexing
print(fruits[-1]) # kiwi
print(fruits[-2]) # orange

# range of indexes like slicing
print(fruits[1:4]) # ['banana', 'cherry', 'orange'] 
                   # 1 включительно, 4 не включительно


# from the start
print(fruits[:3]) # ['apple', 'banana', 'cherry']

# to the end
print(fruits[2:]) # ['cherry', 'orange', 'kiwi']

# check if item exists
if "apple" in fruits:
    print("apple is in the list")