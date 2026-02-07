person = {
    "name": "Alice",
    "age": 20,
    "city": "Almaty",
    "year": 2024
}

# 1) loop through keys
print("Loop through keys:")
for key in person:
    print(key)

# 2) loop through keys - alternative method
print("\nLoop through keys - alternative:")
for key in person.keys():
    print(key)

# 3) loop through values
print("\nLoop through values:")
for value in person.values():
    print(value)

# 4) loop throughkey-value pairs
print("\nLoop through key-value pairs:")
for key, value in person.items():
    print(key, value)