# Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(text):
    result = re.sub(r'([A-Z])', r'_\1', text).lower()
    return result.lstrip('_')

string = "HelloWorldPython"
print(camel_to_snake(string))

# output: hello_world_python