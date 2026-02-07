import copy

original = {
    "name": "Alice",
    "age": 20,
    "city": "Almaty"
}

# using copy()
shallow_copy = original.copy()
print("Original dictionary:")
print(original)
print("\nShallow copy:")
print(shallow_copy)

# modify the copied dictionary
shallow_copy["age"] = 25
print("\nAfter modifying shallow copy:")
print("Original:", original)
print("Shallow copy:", shallow_copy)

