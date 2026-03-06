# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

pattern = r"[a-z]+_[a-z]+"

text = "hello_world test_string Hello_World example_text anotherExample"

matches = re.findall(pattern, text)

print(matches)

# output:
# ['hello_world', 'test_string', 'example_text']