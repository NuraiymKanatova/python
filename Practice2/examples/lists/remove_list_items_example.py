fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
print("Original list:")
print(fruits)

# remove() - removes the first matching value
fruits.remove("banana")
print("\nAfter remove('banana'):")
print(fruits)

# pop() - removes item by index (by default it is last item)
fruits.pop(1)
print("\nAfter pop(1):")
print(fruits)

last_item = fruits.pop()
print("\nAfter pop() without index:")
print(fruits)
print("Removed item:", last_item)

# del - removes item or range by index
del fruits[0]
print("\nAfter del fruits[0]:")
print(fruits)

temp = ["a", "b", "c"]
del temp # del the entire list and printing it would give an error

# clear() - removes all items but keeps the list
fruits.clear()
print("\nAfter clear():")
print(fruits)
