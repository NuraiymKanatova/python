# JSON (JavaScript Object Notation) is a text format for storing and exchanging data
# It language-independent, but Python can read and write it

# JSON data is written as:
# objects -> wrapped {}
# arrays -> wrapped []
# key-value pairs
# key must be in double quotes

{
    "name": "Ivan",
    "age": 18,
    "isStudent": true
}

# keys must be strings
# strings must use double quotes
# no comments allowed
# no trailing commas



# JSON supports only these types:
# string, number (integer or float), object, array, true, false, null

{
    "name": "Anna",
    "age": 20,
    "married": false,
    "skills": ["Python", "SQL"],
    "address": {
        "city": "London",
        "zip": 12345
    }
    "pet": null
}

# in Python: True, False, None
# in JSON:   true, false, null