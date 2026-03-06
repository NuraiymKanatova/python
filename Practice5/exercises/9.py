# Write a Python program to insert spaces between words starting with capital letters.

import re

text = "HelloWorldPythonIsFun"

result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

print(result)

# output: Hello World Python Is Fun