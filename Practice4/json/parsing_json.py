# parsing means converting a JSON string into a Python object

# JSON works with text, Python works with objects
# json.loads() converts text -> Python data

# step 1: import json module
import json

json_text = '{"name": "Ivan", "age": 18, "isStudent": true}'
# this is just a string

# step 2: convert JSON string to Python object
import json
json_text = '{"name": "Ivan", "age": 18, "isStudent": true}'
data = json.loads(json_text)
print(data)          # {'name': 'Ivan', 'age': 18, 'isStudent': True}
print(type(data))    # <class 'dict'>
# now it's a real Python dictionary


# JSON      -> Python mapping
# object    -> dict
# array     -> list
# string    -> str
# number    -> int/float
# true      -> True
# false     -> False
# null      -> None


# accessing parsed data
print(data["name"])   # Ivan
print(data["age"])    # 18


# json.loads() - loads from string
# json.load()  - loads from file