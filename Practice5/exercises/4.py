# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern = r"[A-Z][a-z]+"

text = "Hello world Python Is Fun ABC Test example"

matches = re.findall(pattern, text)

print(matches)

# output: ['Hello', 'Python', 'Is', 'Fun', 'Test']