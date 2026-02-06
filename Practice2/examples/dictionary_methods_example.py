person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Original dictionary:")
print(person)

# 1) get() - returns value for a key, or None if not found
print("\nUsing get():")
print(person.get("name"))  # returns: Alice
print(person.get("country"))  # returns: None - it is not an error

# 2) pop() - removes item by key and returns value
removed_value = person.pop("age")
print("\nAfter pop('age'):")
print(person)
print("Removed value:", removed_value)

# 3) popitem() - removes last inserted item
last_item = person.popitem()
print("\nAfter popitem():")
print(person)
print("Removed item:", last_item)

# 4) update() - updates dictionary with key-value pairs
person.update({"city": "Los Angeles", "country": "USA"})
print("\nAfter update():")
print(person)

# 5) clear() - removes all items from dictionary
person.clear()
print("\nAfter clear():")
print(person)