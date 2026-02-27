# if   json.loads() converts JSON to Python
# then json.dumps() converts Python to JSON

# dumps meaning sump string
# it returns a JSON string, not a file

# step 1: import json
import json
data = {
    "name": "Ivan",
    "age": 18,
    "isStudent": True
}
# this is a Python object

# step 2: convert to JSON string
json_text = json.dumps(data)
print(json_text)          # {"name": "Ivan", "age": 18, "isStudent": true}
print(type(json_text))    # <class 'str'>

# True became true, and the result is a string

# you can format JSON to make it readable
json_text = json.dumps(data, indent=4)
print(json_text)
# now it prints nicely formatted JSON

# Python      -> JSON
# dict        -> object
# lsit        -> array
# str         -> string
# int/float   -> number
# True        -> true
# False       -> false
# None        -> null

# dumps() - returns string
# dump()  - writes to file 