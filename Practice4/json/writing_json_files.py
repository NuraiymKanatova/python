# we don't just convert to a string - we save JSON into a file
# and for that use json.dump()

# step 1: import module
import json

# step 2: create a python data
data = {
    "name": "Ivan",
    "age": 18,
    "skills": ["Python", "HTML"]
}

# step 3: write to a JSON file
# since already created a folder called json, let's assume file path
with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)

# "w" - write mode
# json.dump() writes Python objects as JSON into file
# indent=4 makes it readable
# with open() safely hands file closing


# after running this, your file will contain
{
    "name": "Ivan",
    "age": 18,
    "skills": [
        "Python",
        "HTML"
    ]
}