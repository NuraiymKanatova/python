fruits = ["apple", "banana", "cherry"]
print("\nOriginal list:")
print(fruits)

# append() - add item to the end
fruits.append("orange")
print("\nAfter append():")
print(fruits)

#insert() - add item at a specific item
fruits.insert(1, "kiwi")
print("\nAfter insert():")
print(fruits)

# extend() - add elements from another list
more_fruits = ["mango", "pineapple"]
fruits.extend(more_fruits)
print("\nAfter extend() with another list:")
print(fruits)

# extend() - for tuple (кортеж, неизменяемый тип листа главное отличие - скобки)
extra = ("grape", "pear")
fruits.extend(extra)
print("\nAfter extend() with a tuple:")
print(fruits)