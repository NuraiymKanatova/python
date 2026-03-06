# a set is a set of characters inside a pair of square brackets [] with a special meaning

# [arn] - match specific characters
import re
text = "car ran sun"
matches = re.findall(r"[arn]", text)
print(matches)  # output: ['a', 'r', 'r', 'a', 'n', 'n']
# matches a, r, or n anywhere in the string


# [a-n] - range of characters
import re
text = "apple orange zebra"
matches = re.findall(r"[a-n]", text)
print(matches)  # output: ['a', 'l', 'e', 'a', 'n', 'g', 'e', 'e', 'b', 'a']
# matches any lowercase letter between a and n


# [^arn] - NOT these characters
import re
text = "car ran sun"
matches = re.findall(r"[^arn]", text)
print(matches)  # output: ['c', ' ', ' ', 's', 'u']
# ^ inside a set means exclude these characters


# [0123] - specific digits
import re
text = "012345"
matches = re.findall(r"[0123]", text)
print(matches)  # output: ['0', '1', '2', '3']
# matches 0, 1, 2, or 3


# [0-9] - digit range
import re
text = "Room 203"
matches = re.findall(r"[0-9]", text)
print(matches)  # output: ['2', '0', '3']
# matches any digit from 0 to 9


# [0-5][0-9] - two-digit numbers (00-59)
import re
text = "Times: 05 23 59 72"
matches = re.findall(r"[0-5][0-9]", text)
print(matches)  # output: ['05', '23', '59']
# first digit must be 0-5, second digit 0-9


# [1-zA-Z] - any letter
import re
text = "Hello123"
matches = re.findall(r"[a-zA-Z]", text)
print(matches)  # output: ['H', 'e', 'l', 'l', 'o']
# matches all uppercase and lowercase letters


# [+] - match plus symbol
import re
text = "3 + 5 = 8"
matches = re.findall(r"[+]", text)
print(matches)  # output: ['+']
# inside [ ], symbols like +, *, ., |, () lose their special meaning
# [+] simply matches the plus character