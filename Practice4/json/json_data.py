# wotking with JSON data
# once JSON os loaded with json.load(), 
# it becomes a normal Python object - usually a dictoinary or a list
# after that you treat it like regular Python data

# step 1: load the data
import json
with open("sample-data.json", "r") as file:
    data = json.load(file)
# now data is a dictionary

# accessing values 
print(data["name"])         # Ivan
print(data["skills"])       # ['Python', 'HTML']
print(data["skills"][0])    # Python
# you access it exactly like a Python dictionary

# modify data
data["age"] = 19
data["skills"].append("SQL")
# now the data is updated in memory

# this does NOT automatically update the file

# saving updated data back to file
with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)
# now the file is updated


# working with JSON arrays
# if JSON contains a list:
[
    {"name": "Ivan", "age":18},
    {"name": "Anna", "age": 20}
]

# after loading
with open("sample-data.json", "r") as file:
    data = json.load(file)

for person in data:
    print(person["name"])

# if top-level JSON is an array -> Python gets a list
# JSON is just storage
# Python objetcs are what you actually manipulate
# so actually Read -> Parse -> Modify -> Write back