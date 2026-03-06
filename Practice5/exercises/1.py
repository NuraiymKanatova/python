# Write a Python program that matches a string that has an `'a'` followed by zero or more `'b'`'s.

import re

pattern = r"ab*"

test_strings = ["a", "ab", "abb", "abbb", "ac", "b"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No match")