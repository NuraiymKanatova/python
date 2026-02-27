# if   json.dump() writes Python -> file
# then json.load() reads file    -> Python object

# loads() - from string
# load() - from file

import json
with open("sample-data.json", "r") as file:
    data = json.load(file)

print(data)         # {'name': 'Ivan', 'age': 18, 'skills': ['Python', 'HTML']}
print(type(data))   # <class 'dict'>

# accessing data
print(data["name"])         # Ivan
print(data["skills"][0])    # Python
