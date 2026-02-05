fruits = {"apple", "banana", "cherry"}
print("Original set:")
print(fruits)

# add() - add one item
fruits.add("orange")
print("\nAfter add('orange'):")
print(fruits)

# add() with existing items - will be no error and no change
fruits.add("apple")
print("\nAfter add('apple') again:")
print(fruits)

# update() - add multiple items from another iterable
more_fruits = {"mango", "pineapple"}
fruits.update(more_fruits)
print("\nAfter update() with another set:")
print(fruits)

# update() with list
extra = ["kiwi", "grape"]
fruits.update(extra)
print("\nAfter update() with a list:")
print(fruits)

# the order of items is not guaranteed