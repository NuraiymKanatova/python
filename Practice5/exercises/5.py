# Write a Python program that matches a string that has an `'a'` followed by anything, ending in `'b'`.

import re

pattern = r"a.*b"

test_strings = ["ab", "acb", "axxxb", "a123b", "abbb", "ahello", "cab"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No match")

# output:
# ab -> Match
# acb -> Match
# axxxb -> Match
# a123b -> Match
# abbb -> Match
# ahello -> No match
# cab -> No match