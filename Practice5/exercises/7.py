# Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)

string = "my_variable_name"
result = snake_to_camel(string)

print(result)