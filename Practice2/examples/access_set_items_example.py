fruits = {"apple", "banana", "cherry"}
print(fruits) # print the whole set

# you cannot access items by index
# print(fruits[0]) will be a type error

# so access items using a loop
print("\nAccess items using for loop:")
for fruit in fruits:
    print(fruit)

# and we can check if items exists
print("\nCheck membership:")
print("apple" in fruits)   # will be True
print("orange" in fruits)  # will be False

if "banana" in fruits:
    print("banana is in the set")