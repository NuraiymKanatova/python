# Write a Python program to split a string at uppercase letters.

import re

text = "HelloWorldPythonIsFun"

result = re.split(r"(?=[A-Z])", text)[1:]

print(result)

# output: ['Hello', 'World', 'Python', 'Is', 'Fun']