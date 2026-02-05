person = {
    "name": "Alice",
    "age": 20,
    "city": "Almaty"
}

# access value by key
print(person["name"])
print(person["age"])

# access using get()
print(person.get("city"))

# difference between [] and get()
# print(person["country"]) will give an error
print(person.get("country")) # no error, output - None

print(person.keys())         # get all keys
print(person.values())       # get all values
print(person.items())        # get all key-value pairs

if "age" in person:
    print("Key 'age' exists")