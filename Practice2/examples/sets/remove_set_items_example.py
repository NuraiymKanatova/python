fruits = {"apple", "banana","cherry", "orange"}
print("Origingal set:")
print(fruits)

# remove() - removes specified item (will be error if not found)
fruits.remove("banana")
print("\nAfter remove('banana'):")
print(fruits)

# discard() - removes specified item (no error of not found)
fruits.discard("kiwi")
print("\nAfter discard('kiwi') (no error):")
print(fruits)

# pop() - removes a random item
removed_item = fruits.pop()
print("\nAfter pop():")
print(fruits)
print("Removed item:", removed_item)

# clear() - removes all items
fruits.clear()
print("\nAfter clear():")
print(fruits)
