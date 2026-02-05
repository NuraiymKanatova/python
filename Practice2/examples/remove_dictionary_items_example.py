person = {
    "name": "Alice",
    "age": 20,
    "city": "Almaty",
    "year": 2024
}
print("Original dictionary:")
print(person)

# 1) pop() - remove specific key
removed_value = person.pop("age")
print("\nAfter pop('age'):")
print(person)
print("Removed value:", removed_value)

# 2) popitem() - remove last inserted item
last_item = person.popitem()
print("\nAfter popitem():")
print(person)
print("Removed item:", last_item)

# 3) del - remove specific key
del person["city"]
print("\nAfter del city:")
print(person)

# 4) clear() - remove all items
person.clear()
print("\nAfter clear():")
print(person)