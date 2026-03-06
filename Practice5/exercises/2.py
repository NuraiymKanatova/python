# Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.

import re

pattern = r"ab{2,3}"

test_strings = ["ab", "abb", "abbb", "abbbb", "a", "b"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"{s} -> Match")
    else:
        print(f"{s} -> No match")

# output:
# ab -> No match
# abb -> Match     
# abbb -> Match    
# abbbb -> No match
# a -> No match    
# b -> No match 
