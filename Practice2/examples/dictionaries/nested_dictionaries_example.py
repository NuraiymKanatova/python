student = {
    "name": "John",
    "age": 21,
    "address": {
        "street": "Main St",
        "city": "New York",
        "postal_code": "10001"
    }
}

print("Original dictionary:")
print(student)

# accessing nested dictionary items
print("\nAccessing nested dictionary:")
print(student["address"]["city"])

# adding an item to a nested dictionary
student["address"]["country"] = "USA"
print("\nAfter adding country to address:")
print(student)

# chaning an item in a nested dictionary
student["address"]["city"] = "Los Angeles"
print("\nAfter changing city in address:")
print(student)

# loop through a nested dictionary
print("\nLooping through nested dictionary:")
for key, value in student["address"].items():
    print(key, ":", value)